from django.contrib import admin

from ticket.models import Product, IssueType, Priority, Status, Issue

# Register your models here.
admin.site.register(Product)
admin.site.register(IssueType)
admin.site.register(Priority)
admin.site.register(Status)
admin.site.register(Issue)
