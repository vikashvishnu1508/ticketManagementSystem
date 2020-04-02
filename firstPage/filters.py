from django import forms
import django_filters
from .models import Issue

class IssuesFilter(django_filters.FilterSet):
    summary = django_filters.CharFilter(lookup_expr="icontains")
    # id = django_filters.CharFilter(widget=forms.IntegerField)
    # issueType = django_filters.ChoiceField(widget=forms.ChoiceField)

    class Meta:
        model = Issue
        fields = ['summary',
                  'id',
                  'issueType',
                  'assignedTo',
                  'assignedBy',
                  'status',
                  'priority']