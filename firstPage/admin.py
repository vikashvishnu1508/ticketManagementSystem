from django.contrib import admin

from .models import Department, Role, Product, IssueType, Priority, Status, Issue

# Register your models here.
admin.site.register(Department)
admin.site.register(Role)
admin.site.register(Product)
admin.site.register(IssueType)
admin.site.register(Priority)
admin.site.register(Status)
admin.site.register(Issue)
