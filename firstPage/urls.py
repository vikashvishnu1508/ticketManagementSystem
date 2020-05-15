from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView


urlpatterns = [
    # path('signup', views.SignUp.as_view(), name="signup"),
    # path('login', LoginView.as_view(template_name='firstPage/login.html'), name="login"),
    # path('logout', LogoutView.as_view(template_name='firstPage/logout.html'), name="logout"),
    # path('password_reset', PasswordResetView.as_view(), name="password_reset"),
    # path('password_reset_done', PasswordResetDoneView.as_view(), name="password_reset_done"),
    # path('password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    # path('password_reset_complete', PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    
    # path('', views.index, name="index"),
    # path('createIssue', login_required(login_url='login')(views.CreateIssue.as_view()), name='createIssue'),
    # path('api/raiseTicket', views.CreateIssueAPI.as_view(), name='raiseTicketAPI'),
    # # # path('myTicket', login_required(login_url='login')(views.MyTickets.as_view()), name="myTicket"),
    # path('myTickets', login_required(login_url='login')(views.MyTicketsView.as_view()), name="myTickets"),
    # path('issues', login_required(login_url='login')(views.FilteredIssueListView.as_view()), name="issues"),
    # path('issues/<int:ticket>', views.tickets, name="ticket"),
    # path('issues/<int:ticket>/addUpdate', views.TicketAddUpdate.as_view(), name="addUpdate"),
    # path('issues/<int:ticket>/update', views.UpdatesList.as_view(), name="update"),
    # path('issues/<int:ticket>/assignment', views.AssignmentsList.as_view(), name="assignment"),
    # path('issues/<int:ticket>/assignComment', views.TicketsAssignComment.as_view(), name="assignComment"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
