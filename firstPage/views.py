import os
import copy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib.auth.models import User
from django.views import View
from django.views.generic import ListView, CreateView
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import json

from .models import Department, Role, Product, IssueType, Priority, Status, Issue, Profile, InvestigationDetails, IssueAssignmentDetails, IssueUpdateDetails
from .forms import SignUpForm, IssueCreationForm, AddUpdate, AssignComment
from .filters import IssuesFilter
from .tables import IssueTable
from .serializers import IssueSerializer

from django.conf import settings
from django.conf.urls.static import static
from django_tables2 import RequestConfig, SingleTableView
from django_tables2.export.export import TableExport
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin

# Create your views here.
class SignUp(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'firstPage/signup.html', {'form': form, 'message': None})

    def post(self, request):
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.profile.address = form.cleaned_data.get('address')
            user.profile.phoneNumber = form.cleaned_data.get('phoneNumber')
            user.profile.role = form.cleaned_data.get('role')
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
        return HttpResponseRedirect(reverse('issues'))


class CreateIssue(View):
    def get(self, request):
        form = IssueCreationForm()
        return render(request, 'firstPage/createIssue.html', {'form': form, 'message': 'Issue Form'})

    def post(self, request):
        form = IssueCreationForm(data=request.POST)
        if form.is_valid():
            issue = form.save(commit=False)
            issue.assignedBy = request.user
            issue.status = Status.objects.get(pk=1)
            issue.save()
        return render(request, 'firstPage/createIssue.html', {'message': 'Issue Created sucessfuly!'})

class CreateIssueAPI(APIView):
    def post(self, request, format=None):
        serializer = IssueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            jsonobj = serializer.data
            jsonobj['id'] = serializer.instance.pk
            return Response(jsonobj, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TicketAddUpdate(View):
    def get(self, request, ticket):
        form = AddUpdate()
        return render(request, 'firstPage/addUpdate.html', {'form': form})

    def post(self, request, ticket):
        form = AddUpdate(request.POST, request.FILES)
        if form.is_valid():
            update = form.save(commit=False)
            update.addedBy = request.user
            update.issue = Issue.objects.get(pk=ticket)
            update.sequence = len(IssueUpdateDetails.objects.filter(issue=ticket)) + 1
            update.save()
        return HttpResponseRedirect(reverse('ticket', args=[ticket]))


class UpdatesList(ListView):
    model = IssueUpdateDetails
    context_object_name = 'updates'
    template_name = 'firstPage/update.html'
    paginate_by = 1

    def get_queryset(self):
        return IssueUpdateDetails.objects.filter(issue=self.kwargs['ticket'])

class AssignmentsList(ListView):
    model = IssueAssignmentDetails
    context_object_name = 'assignments'
    template_name = 'firstPage/assigment.html'
    paginate_by = 1

    def get_queryset(self):
        return IssueAssignmentDetails.objects.filter(issue=self.kwargs['ticket'])


class TicketsAssignComment(CreateView):
    form_class = AssignComment
    model = IssueAssignmentDetails
    # fields = ['assignedTo','comment', 'attachments']
    template_name = 'firstPage/assignComment.html'

    def form_valid(self, form):
        issue = Issue.objects.get(pk=self.kwargs['ticket'])
        form.instance.assignedBy = self.request.user
        form.instance.issue = issue
        form.instance.sequence = len(IssueAssignmentDetails.objects.filter(issue=self.kwargs['ticket'])) + 1
        issue.assignedTo = form.instance.assignedTo
        issue.assignedBy = form.instance.assignedBy
        issue.save(update_fields=['assignedTo', 'assignedBy'])
        form.save()
        return super(TicketsAssignComment, self).form_valid(form)

    def get_success_url(self):
        return reverse('ticket', args=[self.kwargs['ticket']])


class FilteredIssueListView(SingleTableMixin, FilterView):
    table_class = IssueTable
    model = Issue
    template_name = "firstPage/issue.html"
    filterset_class = IssuesFilter
    paginate_by = 10

# need to edit this part
class MyTicketsView(SingleTableMixin, FilterView):
    table_class = IssueTable
    model = Issue
    template_name = "firstPage/issue.html"
    filterset_class = IssuesFilter
    paginate_by = 10
    
    def get(self, request, *args, **kwargs):
        self.current_request = request
        return super().get(request, *args, **kwargs)
    
    def get_queryset(self):
        if self.current_request.GET:
            filter_values = copy.copy(self.current_request.GET)
            filter_values['assignedTo'] = str(self.current_request.user.id)
            issues = IssuesFilter(filter_values, queryset=Issue.objects.all())
            return issues.qs
        else:
            issues = IssuesFilter({'assignedTo': self.current_request.user}, queryset=Issue.objects.all())
            return issues.qs

def index(request):
    return HttpResponseRedirect('issues')


def tickets(request, ticket):
    try:
        issue = Issue.objects.get(pk=ticket)
        customerDetails = User.objects.get(pk=issue.assignedBy.id)
        investigationDetails = InvestigationDetails.objects.filter(id=ticket)
        issueAssignmentDetails = IssueAssignmentDetails.objects.filter(issue=ticket)
        issueUpdateDetails = IssueUpdateDetails.objects.filter(issue=ticket)
        context= {
            'user': request.user,
            'message': 'LogedIn',
            'issue': issue,
            'assigner': customerDetails,
            'investigationDetails': investigationDetails,
            'issueAssignmentDetails': issueAssignmentDetails,
            'issueUpdateDetails': issueUpdateDetails
        }
        return render(request, 'firstPage/ticket.html', context)
    except:
        raise Http404("Please try again after sometime")
