from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('', views.index, name="index"),
    path('<int:ticket>', views.tickets, name="ticket"),
    path('myTicket', views.myTickets, name="myTicket"),
    path('<int:ticket>/addUpdate', views.TicketAddUpdate.as_view(), name="addUpdate"),
    path('login', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
    path('createIssue', views.CreateIssue.as_view(), name='createIssue'),
    path('<int:ticket>/update', views.UpdatesList.as_view(), name="update"),
    path('<int:ticket>/assignment', views.AssignmentsList.as_view(), name="assignment"),
    path('<int:ticket>/assignComment', views.TicketsAssignComment.as_view(), name="assignComment"),
    path('issues', login_required(login_url='login')(views.FilteredIssueListView.as_view()), name="issues"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
