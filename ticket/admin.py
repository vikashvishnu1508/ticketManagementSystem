from django.contrib import admin

from ticket.models import Product, IssueType, Priority, Status, Issue, IssueUpdateDetails, IssueAssignmentDetails, InvestigationDetails

# Register your models here.
admin.site.register(Product)
admin.site.register(IssueType)
admin.site.register(Priority)
admin.site.register(Status)
admin.site.register(Issue)
admin.site.register(IssueUpdateDetails)
admin.site.register(IssueAssignmentDetails)
admin.site.register(InvestigationDetails)
