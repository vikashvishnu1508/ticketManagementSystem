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



# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     location = models.CharField(max_length=30, blank=True, null=True)
#     birth_date = models.DateField(null=True, blank=True)
#     address = models.CharField(max_length=8000, blank=True, null=True)
#     phoneNumber = models.CharField(max_length=10)
#     role = models.ForeignKey(Role,
#                              on_delete=models.CASCADE,
#                              related_name='role',
#                              null=True,
#                              blank=True)
    
#     def __str__(self):
#         return f'{self.user} - {self.location}'


# @receiver(post_save, sender=User)
# def update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.profile.save()
