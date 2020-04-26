import os
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib.auth.models import User
from django.views import View
from django.views.generic import ListView, CreateView


from .models import Department, Role, Product, IssueType, Priority, Status, Issue, Profile, InvestigationDetails, IssueAssignmentDetails, IssueUpdateDetails
from .forms import SignUpForm, IssueCreationForm, AddUpdate, AssignComment
from .filters import IssuesFilter
from .tables import IssueTable

from django.conf import settings
from django.conf.urls.static import static
from django_tables2 import RequestConfig, SingleTableView
from django_tables2.export.export import TableExport
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
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
            return HttpResponseRedirect(reverse('index'))
        else:
            form = SignUpForm()
            return render(request, 'firstPage/index.html', {'form': form, 'message': None})
    else:
        issues = IssuesFilter(request.GET, queryset=Issue.objects.all())
        table = IssueTable(issues.qs)
        RequestConfig(request).configure(table)
        table.paginate(page=request.GET.get("page", 1), per_page=5)
        context = {
            'user': request.user,
            'message': 'LogedIn',
            'filter': issues,
            'table': table
        }
        return render(request, 'firstPage/index.html', context)


def myTickets(request):
    issues = IssuesFilter({'assignedTo': request.user}, queryset=Issue.objects.all())
    table = IssueTable(issues.qs)
    RequestConfig(request).configure(table)
    table.paginate(page=request.GET.get("page", 1), per_page=5)
    context = {
        'user': request.user,
        'message': 'LogedIn',
        'filter': issues,
        'table': table
    }
    return render(request, 'firstPage/index.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'firstPage/login.html', {'message': 'Invalid credential'})
    else:
        return render(request, 'firstPage/login.html')

def logout_view(request):
    logout(request)
    return render(request, 'firstPage/logout.html', {'message': 'Logout sucessfuly!'})


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
        # print(self.kwargs['ticket'])
        return super(TicketsAssignComment, self).form_valid(form)
    
    def get_success_url(self):
        return reverse('ticket', args=[self.kwargs['ticket']])


class FilteredIssueListView(SingleTableMixin, FilterView):
    table_class = IssueTable
    model = Issue
    template_name = "firstPage/issue.html"
    filterset_class = IssuesFilter
    paginate_by = 10

