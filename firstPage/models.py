from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length = 100,
                            null=False,
                            blank=False,
                            unique=True)
    
    def __str__(self):
        return f'{self.name}'


class Role(models.Model):
    name = models.CharField(max_length = 100,
                            null=False,
                            blank=False)
    department = models.ForeignKey(Department,
                                   on_delete=models.CASCADE,
                                   related_name='department',
                                   null=False,
                                   blank=False)
    
    def __str__(self):
        return f'{self.department} - {self.name}'



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=30, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=8000, blank=True, null=True)
    phoneNumber = models.CharField(max_length=10)
    role = models.ForeignKey(Role,
                             on_delete=models.CASCADE,
                             related_name='role',
                             null=True,
                             blank=True)
    
    def __str__(self):
        return f'{self.user} - {self.location}'


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


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
                             related_name='ticketAssignedTo')
    assignedBy = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             null=False,
                             blank=False,
                             related_name='ticketAssignedBy')
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
                             related_name='assignmentAssignedTo')
    assignedBy = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             null=False,
                             blank=False,
                             related_name='assignmentAssignedBy')
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
                             related_name='addedBy')
    update = models.TextField()
    attachments = models.FileField(upload_to='documents/Updates/', null=True, blank=True)
    
    def __str__(self):
        return f'{self.issue} - {self.update}'

