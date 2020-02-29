from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Department, Role, UserDetails
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