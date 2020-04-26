from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelChoiceField
from django.forms import ModelForm

from .models import Department, Role, Product, IssueType, Priority, Status, Issue, IssueUpdateDetails, IssueAssignmentDetails

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
    
    birth_date = forms.DateField(help_text="Required. Format: YYYY-MM-DD",
                                 widget=forms.DateInput(attrs={'id':'birth-date',
                                                                'class':'form-control col-md-6 float-left',
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


class IssueCreationForm(ModelForm):
    product = forms.ModelChoiceField(Product.objects.all(),
                            widget=forms.Select(attrs={'class':'ddl form-control',
                                                        'placeholder':'Project'}),
                            to_field_name="productName",
                            empty_label=None)
    issueType = forms.ModelChoiceField(IssueType.objects.all(),
                            widget=forms.Select(attrs={'class':'ddl form-control',
                                                        'placeholder':'Issue Type'}),
                            to_field_name="issueType",
                            empty_label=None)
    summary = forms.CharField(max_length=2000, required=False, help_text='Required.',
                                 widget=forms.TextInput(attrs={'class':'form-control',
                                                               'placeholder':'Summary'}))
    description = forms.CharField(help_text='Required.',
                                 widget=forms.Textarea(attrs={'class':'form-control',
                                                               'placeholder':'Description',}))
    assignedTo = forms.ModelChoiceField(User.objects.all(),
                            widget=forms.Select(attrs={'class':'ddl form-control',
                                                        'placeholder':'Assigned To'}),
                            to_field_name="username",
                            empty_label="Select Assignee")
    priority = forms.ModelChoiceField(Priority.objects.all(),
                            widget=forms.Select(attrs={'class':'ddl form-control',
                                                        'placeholder':'Priority'}),
                            to_field_name="priority",
                            empty_label=None)

    class Meta:
        model = Issue
        fields = (  'product',
                    'issueType',
                    'summary',
                    'description',
                    'assignedTo',
                    # 'status',
                    'priority',)


class AddUpdate(ModelForm):
    update = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control',
                                                            'placeholder':'Add Update',}))
    attachments = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control-file',
                                                            'placeholder':'Upload files',}))

    class Meta:
        model = IssueUpdateDetails
        fields = ('update',
                  'attachments',)



class AssignComment(ModelForm):
    assignedTo = forms.ModelChoiceField(User.objects.all(),
                            widget=forms.Select(attrs={'class':'ddl form-control',
                                                        'placeholder':'Assigned To'}),
                            to_field_name="username",
                            empty_label="Select Assignee")
    comment = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control-file',
                                                        'placeholder':'Add asignment comment',}))
    attachments = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control-file',
                                                            'placeholder':'Upload files',}))

    class Meta:
        model = IssueAssignmentDetails
        fields = ('assignedTo',
                  'comment',
                  'attachments')
