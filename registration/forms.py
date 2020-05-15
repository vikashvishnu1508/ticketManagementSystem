from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelChoiceField
from django.forms import ModelForm

from registration.models import Department, Role

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Required.',
                                 widget=forms.TextInput(attrs={'class':'form-control col-md-6 float-left',
                                                               'placeholder':'First Name *'}))
    last_name = forms.CharField(max_length=30, required=False, help_text='Required.',
                                 widget=forms.TextInput(attrs={'class':'form-control col-md-6 float-right',
                                                               'placeholder':'Last Name *'}))
    
    username = forms.CharField(max_length=30, required=False, help_text='Required.',
                                 widget=forms.TextInput(attrs={'class':'form-control col-md-6 float-left',
                                                               'placeholder':'Username *'}))
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.',
                                 widget=forms.EmailInput(attrs={'class':'form-control col-md-6 float-right',
                                                               'placeholder':'Email Address *'}))
    
    password1 = forms.CharField(max_length=254, help_text='Required',
                                 widget=forms.PasswordInput(attrs={'class':'form-control col-md-6 float-left',
                                                               'placeholder':'Password *'}))
    password2 = forms.CharField(max_length=254, help_text='Required.',
                                 widget=forms.PasswordInput(attrs={'class':'form-control col-md-6 float-right',
                                                               'placeholder':'Re-enter password *'}))
    
    class Meta:
        model = User
        fields = ('first_name',
                  'last_name',
                  'username',
                  'email',
                  'password1',
                  'password2',)
