from django import forms
import django_filters
from ticket.models import *
from crispy_forms.helper import FormHelper

ASSIGNMENT_USER = User.objects.all()

class IssuesFilter(django_filters.FilterSet):
    summary = django_filters.CharFilter(label="Summary", lookup_expr="icontains")
    status = django_filters.ModelChoiceFilter(queryset=Status.objects.all(), empty_label="Status")
    priority = django_filters.ModelChoiceFilter(queryset=Priority.objects.all(), empty_label="Priority")
    product = django_filters.ModelChoiceFilter(queryset=Product.objects.all(), empty_label="Product")
    issueType = django_filters.ModelChoiceFilter(queryset=IssueType.objects.all(), empty_label="IssueType")
    assignedTo = django_filters.ModelChoiceFilter(queryset=ASSIGNMENT_USER, empty_label="Assigned To")
    assignedBy = django_filters.ModelChoiceFilter(queryset=ASSIGNMENT_USER, empty_label="Assigned By")

    class Meta:
        model = Issue
        fields = ['id',
                  'summary',
                  'status',
                  'priority',
                  'product',
                  'issueType',
                  'assignedTo',
                  'assignedBy',
                  'creadtedDate',
                  'closedDate',]