from django import forms
import django_filters
from .models import *
from crispy_forms.helper import FormHelper

class IssuesFilter(django_filters.FilterSet):
    summary = django_filters.CharFilter(label="Summary", lookup_expr="icontains")

    class Meta:
        model = Issue
        fields = ['id',
                  'summary',
                  'status',
                  'priority',
                  'issueType',
                  'assignedTo',
                  'assignedBy']