from django.urls import path, re_path
from api import views
from django.contrib.auth.decorators import login_required

app_name = 'api'

urlpatterns = [
    path('raiseTicket', views.CreateIssueAPI.as_view(), name='raiseTicketAPI'),
]
