from django.db import models
from django.contrib.auth.models import User

from django.urls import reverse
# Create your models here.

class Product(models.Model):
    productName = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.productName}'


class IssueType(models.Model):
    issueType = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.issueType}'


class Priority(models.Model):
    priority = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.priority}'


class Status(models.Model):
    status = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.status}'


class Issue(models.Model):
    product = models.ForeignKey(Product,
                             on_delete=models.CASCADE,
                             null=False,
                             blank=False,
                             related_name='relatedProduct')
    issueType = models.ForeignKey(IssueType,
                             on_delete=models.CASCADE,
                             null=False,
                             blank=False,
                             related_name='requestType')
    summary = models.CharField(max_length=2000)
    description = models.TextField()
    assignedTo = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             null=False,
                             blank=False,
                             related_name='ticketAssignee')
    assignedBy = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             null=False,
                             blank=False,
                             related_name='ticketAssigner')
    creadtedDate = models.DateTimeField(auto_now=False, auto_now_add=True)
    modifiedDate = models.DateTimeField(auto_now=False, auto_now_add=True)
    closedDate = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    status = models.ForeignKey(Status,
                             on_delete=models.CASCADE,
                             null=False,
                             blank=False,
                             related_name='ticketStatus')
    priority = models.ForeignKey(Priority,
                             on_delete=models.CASCADE,
                             null=False,
                             blank=False,
                             related_name='ticketPriority')

    def __str__(self):
        return f'{self.summary} - {self.status}'

    def get_absolute_url(self):
        return reverse("ticket", kwargs={"pk": self.pk})


class InvestigationDetails(models.Model):
    issue = models.ForeignKey(Issue,
                             on_delete=models.CASCADE,
                             null=False,
                             blank=False,
                             related_name='ticketStatus')
    investigationTaken = models.TextField()

    def __str__(self):
        return f'{self.issue} - {self.investigationTaken}'


class IssueAssignmentDetails(models.Model):
    issue = models.ForeignKey(Issue,
                             on_delete=models.CASCADE,
                             null=False,
                             blank=False,
                             related_name='assignmentIssue')
    sequence = models.IntegerField()
    createdDate = models.DateTimeField(auto_now=True, auto_now_add=False)
    assignedTo = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             null=False,
                             blank=False,
                             related_name='assignmentAssigner')
    assignedBy = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             null=False,
                             blank=False,
                             related_name='assignmentAssignee')
    comment = models.TextField()
    attachments = models.FileField(upload_to='documents/Assignment/', null=True, blank=True)

    def __str__(self):
        return f'{self.issue} - {self.comment}'


class IssueUpdateDetails(models.Model):
    issue = models.ForeignKey(Issue,
                             on_delete=models.CASCADE,
                             null=False,
                             blank=False,
                             related_name='updateRelatedIssue')
    sequence = models.IntegerField()
    dateAdded = models.DateTimeField(auto_now=True, auto_now_add=False)
    addedBy = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             null=False,
                             blank=False,
                             related_name='updatedBy')
    update = models.TextField()
    attachments = models.FileField(upload_to='documents/Updates/', null=True, blank=True)

    def __str__(self):
        return f'{self.issue} - {self.update}'
