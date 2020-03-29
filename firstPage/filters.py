import django_filters
from .models import Issue

class IssuesFilter(django_filters.FilterSet):
    
    class Meta:
        model = Issue
        fields = ['summary',
                  'id',]