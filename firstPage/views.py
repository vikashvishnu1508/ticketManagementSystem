from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Department, Role
from .forms import SignUpForm
# Create your views here.
def index(request):
    # context = {
    #     'users': User.objects.all(),
    #     'roles' : Role.objects.all(),
    #     'departments' : Department.objects.all()
    # }
    # return render(request, 'firstPage/index.html', context)
    if not request.user.is_authenticated:
        return render(request, 'firstPage/login.html', {'message': None})
    context = {
        'user': request.user
    }
    return render(request, 'firstPage/user.html', context)

def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'firstPage/login.html', {'message': 'Invalid credential'})

def logout_view(request):
    logout(request)
    return render(request, 'firstPage/logout.html', {'message': 'Logout sucessfuly'})

def signup_view(request):
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
    return render(request, 'firstPage/signup.html', {'form': form})