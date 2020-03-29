from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:ticket>', views.tickets, name="ticket"),
    path('<int:ticket>/addUpdate', views.ticketsAddUpdate, name="addUpdate"),
    path('<int:ticket>/assignComment', views.ticketsAssignComment, name="assignComment"),
    path('login', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
    path('createIssue', views.create_issue, name='createIssue')
]
