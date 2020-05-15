import django_tables2 as tables
from ticket.models import *
from django_tables2 import SingleTableView


class IssueTable(tables.Table):
    status = tables.Column(accessor="status__status", orderable=True)
    summary = tables.Column(orderable=True)
    closedDate = tables.Column(default='Still open')

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
                  'closedDate']
        attrs = {"class": "table table-striped table-bordered table-hover",
                 'thead' : {'class': 'thead-dark'}}
        row_attrs = {
            "data-id": lambda record: record.pk
        }