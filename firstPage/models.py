from django.db import models

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
                                   blank=False,
                                   default=0)
    
    def __str__(self):
        return f'{self.department} - {self.name}'


class User(models.Model):
    empID = models.IntegerField()
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=8000)
    phoneNumber = models.CharField(max_length=10)
    role = models.ForeignKey(Role,
                             on_delete=models.CASCADE,
                             related_name='role',
                             null=False,
                             blank=False,
                             default=0)
    location = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.name} - {self.location} - {self.role}'

