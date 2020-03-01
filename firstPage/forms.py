from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelChoiceField

from .models import Role

# test = Role
# test1 = Role.objects.all()

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Required.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Required.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    birth_date = forms.DateField(help_text="Required. Format: YYYY-MM-DD")
    address = forms.CharField(max_length=8000, help_text='Required.')
    phoneNumber = forms.CharField(max_length=10, help_text='Required.')
    role = forms.ModelChoiceField(Role.objects.all(),
                            widget=forms.Select(attrs={'class':'ddl'}),
                            to_field_name="name",
                            empty_label=None)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'birth_date', 'address', 'phoneNumber', 'role',)

    # def __init__(self, *args, **kwargs):
    #     super(Role, self).__init__(*args, **kwargs)
    #     self.fields['role'].quertset = Role.objects.all()