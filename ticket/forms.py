from django import forms
from django.forms import ModelChoiceField
from django.forms import ModelForm

from ticket.models import *

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
                    'priority',)


class AddUpdate(ModelForm):
    update = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control',
                                                            'placeholder':'Add Update',}))
    attachments = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control-file',
                                                            'placeholder':'Upload files',}))

    def __init__(self, *args, **kwargs):
        super(AddUpdate, self).__init__(*args, **kwargs)
        self.fields['attachments'].required = False

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

    def __init__(self, *args, **kwargs):
        super(AssignComment, self).__init__(*args, **kwargs)
        self.fields['attachments'].required = False

    class Meta:
        model = IssueAssignmentDetails
        fields = ('assignedTo',
                  'comment',
                  'attachments')
