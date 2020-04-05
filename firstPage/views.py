from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Department, Role, Product, IssueType, Priority, Status, Issue, Profile, InvestigationDetails, IssueAssignmentDetails, IssueUpdateDetails
from .forms import SignUpForm, IssueCreationForm, AddUpdate, AssignComment
from .filters import IssuesFilter
from .tables import IssueTable

from django.conf import settings
from django.conf.urls.static import static
from django_tables2 import RequestConfig
from django_tables2.export.export import TableExport

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
#     if len(request.GET) == 0:
#             issues = IssuesFilter({'assignedTo': request.user}, queryset=Issue.objects.all())
#         else:
#             issues = IssuesFilter(request.GET, queryset=Issue.objects.all())
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

def create_issue(request):
    if request.method == 'POST':
            form = IssueCreationForm(data=request.POST)
            if form.is_valid():
                issue = form.save(commit=False)
                issue.assignedBy = request.user
                issue.status = Status.objects.get(pk=1)
                issue.save()
            return render(request, 'firstPage/createIssue.html', {'message': 'Issue Created sucessfuly!'})
    else:
        form = IssueCreationForm()
        return render(request, 'firstPage/createIssue.html', {'form': form, 'message': 'Issue Form'})

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

def ticketsAddUpdate(request, ticket):
    if request.method == 'POST':
        form = AddUpdate(data=request.POST)
        if form.is_valid():
            update = form.save(commit=False)
            update.addedBy = request.user
            update.issue = Issue.objects.get(pk=ticket)
            update.sequence = len(IssueUpdateDetails.objects.filter(issue=ticket)) + 1
            update.save()
        return HttpResponseRedirect(reverse('ticket', args=[ticket]))
    else:
        form = AddUpdate()
        return render(request, 'firstPage/addUpdate.html', {'form': form})


def ticketsAssignComment(request, ticket):
    if request.method == 'POST':
        form = AssignComment(data=request.POST)
        if form.is_valid():
            issue = Issue.objects.get(pk=ticket)
            comment = form.save(commit=False)
            comment.assignedBy = request.user
            comment.issue = issue
            comment.sequence = len(IssueAssignmentDetails.objects.filter(issue=ticket)) + 1
            issue.assignedTo = comment.assignedTo
            issue.assignedBy = comment.assignedBy
            issue.save(update_fields=['assignedTo', 'assignedBy'])
            comment.save()
        return HttpResponseRedirect(reverse('ticket', args=[ticket]))
    else:
        form = AssignComment()
        return render(request, 'firstPage/assignComment.html', {'form': form})

