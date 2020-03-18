from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelChoiceField

from .models import Role

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
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.',
                                 widget=forms.EmailInput(attrs={'class':'form-control col-md-6 float-right',
                                                               'placeholder':'Email Address *'}))
    
    password1 = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.',
                                 widget=forms.PasswordInput(attrs={'class':'form-control col-md-6 float-left',
                                                               'placeholder':'Password *'}))
    password2 = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.',
                                 widget=forms.PasswordInput(attrs={'class':'form-control col-md-6 float-right',
                                                               'placeholder':'Re-enter password *'}))
    
    birth_date = forms.DateField(help_text="Required. Format: YYYY-MM-DD",
                                 widget=forms.DateInput(attrs={'class':'form-control col-md-6 float-left',
                                                               'placeholder':'Please enter Birth Date *'}))
    phoneNumber = forms.CharField(max_length=10, help_text='Required.',
                                 widget=forms.TextInput(attrs={'class':'form-control col-md-6 float-right',
                                                               'placeholder':'Phone Number *'}))
    
    address = forms.CharField(max_length=8000, help_text='Required.',
                                 widget=forms.Textarea(attrs={'class':'form-control',
                                                               'placeholder':'Address *',
                                                               'style': 'height: 5em;'}))
    
    role = forms.ModelChoiceField(Role.objects.all(),
                            widget=forms.Select(attrs={'class':'ddl form-control',
                                                        'placeholder':'Please select a role *'}),
                            to_field_name="name",
                            empty_label=None)
    class Meta:
        model = User
        fields = ('first_name',
                  'last_name',
                  'username',
                  'email',
                  'password1',
                  'password2',
                  'birth_date',
                  'phoneNumber',
                  'address',
                  'role',)

    # def __init__(self, *args, **kwargs):
    #     super(Role, self).__init__(*args, **kwargs)
    #     self.fields['role'].quertset = Role.objects.all()
