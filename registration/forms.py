from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelChoiceField
from django.forms import ModelForm

from registration.models import Department, Role

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30,
                                 widget=forms.TextInput(attrs={'class':'form-control',
                                                               'placeholder':'First Name *'}))
    last_name = forms.CharField(max_length=30,
                                 widget=forms.TextInput(attrs={'class':'form-control',
                                                               'placeholder':'Last Name *'}))
    
    username = forms.CharField(max_length=30,
                                 widget=forms.TextInput(attrs={'class':'form-control',
                                                               'placeholder':'Username *'}))
    email = forms.EmailField(max_length=150,
                                 widget=forms.EmailInput(attrs={'class':'form-control',
                                                               'placeholder':'Email Address *'}))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control',
                                                               'placeholder':'Password *'}),
                                help_text="<ul><li>Your password can&#39;t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can&#39;t be a commonly used password.</li><li>Your password can&#39;t be entirely numeric.</li></ul>")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control',
                                                               'placeholder':'Re-enter password *'}))
    
    class Meta:
        model = User
        fields = ('first_name',
                  'last_name',
                  'username',
                  'email',
                  'password1',
                  'password2',)
