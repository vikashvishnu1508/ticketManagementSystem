from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import Http404, HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import View

from registration.models import Department, Role
from registration.forms import SignUpForm


# Create your views here.
class SignUp(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'registration/signup.html', {'form': form, 'message': None})

    def post(self, request):
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect(reverse('ticket:issues'))
        return render(request, 'registration/signup.html', {'form': form, 'message': None})


def index(request):
    return render(request, 'registration/home.html')