from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelChoiceField

from .models import Role

# test = Role
# test1 = Role.objects.all()

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=False, help_text='Required.',
                                 widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=30, required=False, help_text='Required.',
                                 widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=30, required=False, help_text='Required.',
                                 widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.',
                                 widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.',
                                 widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.',
                                 widget=forms.PasswordInput(attrs={'class':'form-control'}))
    birth_date = forms.DateField(help_text="Required. Format: YYYY-MM-DD",
                                 widget=forms.DateInput(attrs={'class':'form-control'}))
    address = forms.CharField(max_length=8000, help_text='Required.',
                                 widget=forms.Textarea(attrs={'class':'form-control'}))
    phoneNumber = forms.CharField(max_length=10, help_text='Required.',
                                 widget=forms.TextInput(attrs={'class':'form-control'}))
    role = forms.ModelChoiceField(Role.objects.all(),
                            widget=forms.Select(attrs={'class':'ddl form-control'}),
                            to_field_name="name",
                            empty_label=None)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'birth_date', 'address', 'phoneNumber', 'role',)

    # def __init__(self, *args, **kwargs):
    #     super(Role, self).__init__(*args, **kwargs)
    #     self.fields['role'].quertset = Role.objects.all()
