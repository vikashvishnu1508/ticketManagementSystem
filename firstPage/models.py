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
    # empID = models.IntegerField(null=True, blank=True)
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


class ProductCategory(models.Model):
    categoryName = models.CharField(max_length=1000)
    
    def __str__(self):
        return f'{self.categoryName}'


class Product(models.Model):
    categoryName = models.ForeignKey(ProductCategory,
                                     on_delete=models.CASCADE,
                                     related_name='category',
                                     null=False,
                                     blank=False
                                    #  ,
                                    #  default=0
                                     )
    productName = models.CharField(max_length=1000)
    modelNumber = models.CharField(max_length=1000,
                                   null=False,
                                   default='1.0')
    
    def __str__(self):
        return f'{self.categoryName} - {self.productName} - {self.modelNumber}'


class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=8000)
    location = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=10)
    
    def __str__(self):
        return f'{self.name} - {self.location} - {self.phoneNumber}'


class Partner(models.Model):
    company = models.ForeignKey(Company,
                                on_delete=models.CASCADE,
                                null=False,
                                blank=False,
                                default=0,
                                related_name='partnerCompany')
    serviceType = models.CharField(max_length=1000)
    isActive = models.BooleanField(null=False,
                                   blank=False,
                                   default=False)
    
    def __str__(self):
        return f'{self.company} - Service : {self.serviceType} - Active : {self.isActive}'


class Client(models.Model):
    partner = models.ForeignKey(Partner,
                                on_delete=models.CASCADE,
                                null=False,
                                blank=False,
                                # default=0,
                                related_name='clientPartner')
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             null=False,
                             blank=False,
                            #  default=0,
                             related_name='actulClientUser')
    company = models.ForeignKey(Company,
                                on_delete=models.CASCADE,
                                null=False,
                                blank=False,
                                # default=0,
                                related_name='clientCompany')
    product = models.ForeignKey(Product,
                             on_delete=models.CASCADE,
                             null=False,
                             blank=False,
                            #  default=0,
                             related_name='clientProduct')
    
    def __str__(self):
        return f'{self.company} - {self.product}'


class Severity(models.Model):
    severity = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.severity}'

class ServiceDeliveryLevel(models.Model):
    supportLevel = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.supportLevel}'


class Ticket(models.Model):
    client = models.ForeignKey(Client,
                             on_delete=models.CASCADE,
                             null=False,
                             blank=False,
                             default=0,
                             related_name='ticket_s_Client')
    serviceCategory = models.CharField(max_length=8000)
    severity = models.ForeignKey(Severity,
                             on_delete=models.CASCADE,
                             null=False,
                             blank=False,
                             default=0,
                             related_name='ticket_s_severity')
    issueSubject = models.CharField(max_length=8000)
    issueDescription = models.TextField()
    creadtedDate = models.DateTimeField(auto_now=False, auto_now_add=True)
    modifiedDate = models.DateTimeField(auto_now=False, auto_now_add=True)
    status = models.CharField(max_length=100)
    closedDate = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
    assignedTo = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             null=False,
                             blank=False,
                             default=0,
                             related_name='ticketAssignedTo')
    assignedBy = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             null=False,
                             blank=False,
                             default=0,
                             related_name='ticketAssignedBy')
    serviceDeliveryLevel = models.ForeignKey(ServiceDeliveryLevel,
                             on_delete=models.CASCADE,
                             null=False,
                             blank=False,
                             default=0,
                             related_name='serviceLevel')
    
    def __str__(self):
        return f'{self.client} - {self.issueSubject}'


class TicketCommentDetails(models.Model):
    ticket = models.ForeignKey(Ticket,
                             on_delete=models.CASCADE,
                             null=False,
                             blank=False,
                             default=0,
                             related_name='commentForTicket')
    sequence = models.IntegerField()
    createdDate = models.DateTimeField(auto_now=True, auto_now_add=False)
    assignedTo = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             null=False,
                             blank=False,
                             default=0,
                             related_name='commentAssignedTo')
    assignedBy = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             null=False,
                             blank=False,
                             default=0,
                             related_name='commentAssignedBy')
    comment = models.TextField()
    status = models.CharField(max_length=100)
    modifiedDate = models.DateTimeField(auto_now=True,auto_now_add=False)
    
    def __str__(self):
        return f'{self.ticket} - {self.comment}'









