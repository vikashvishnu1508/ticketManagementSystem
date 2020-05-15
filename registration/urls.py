from django.urls import path, re_path
from registration import views
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView

app_name = 'registration'

urlpatterns = [
    path(r'signup', views.SignUp.as_view(), name="regsignup"),
    path('login', LoginView.as_view(template_name='registration/login.html'), name="login"),
    path('logout', LogoutView.as_view(template_name='registration/logout.html'), name="logout"),
    path('password_reset', PasswordResetView.as_view(), name="password_reset"),
    path('password_reset_done', PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('password_reset_complete', PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
