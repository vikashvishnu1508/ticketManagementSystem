from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name="index"),
    path('<int:ticket>', views.tickets, name="ticket"),
    path('myTicket', views.myTickets, name="myTicket"),
    path('<int:ticket>/addUpdate', views.ticketsAddUpdate, name="addUpdate"),
    path('<int:ticket>/assignComment', views.ticketsAssignComment, name="assignComment"),
    path('login', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
    path('createIssue', views.create_issue, name='createIssue'),
    path('<int:ticket>/update/<int:sequence>', views.Updates.as_view(), name="update")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
