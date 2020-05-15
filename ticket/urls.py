from django.urls import path, re_path
from ticket import views
from django.contrib.auth.decorators import login_required

app_name = 'ticket'

urlpatterns = [
    path('createIssue', login_required(login_url='login')(views.CreateIssue.as_view()), name='createIssue'),
    path('myTickets', login_required(login_url='login')(views.MyTicketsView.as_view()), name="myTickets"),
    path('issues', login_required(login_url='login')(views.FilteredIssueListView.as_view()), name="issues"),
    path('issues/<int:ticket>', views.tickets, name="ticket"),
    path('issues/<int:ticket>/addUpdate', views.TicketAddUpdate.as_view(), name="addUpdate"),
    path('issues/<int:ticket>/update', views.UpdatesList.as_view(), name="update"),
    path('issues/<int:ticket>/assignment', views.AssignmentsList.as_view(), name="assignment"),
    path('issues/<int:ticket>/assignComment', views.TicketsAssignComment.as_view(), name="assignComment"),
]
