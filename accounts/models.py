# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
        ('enterprise', 'Enterprise'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES,default='user')
   
    
   

    # Set related_name to avoid clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set', 
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
    
    def __str__(self):
        return f"User ID: {self.id}"
  
 
    


from django.db import models


class MyFormData(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='myformdata', null=True)
    company = models.CharField(max_length=100)
    your_name = models.CharField(max_length=100)
    company_gstin = models.CharField(max_length=50)
    company_address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    client_company = models.CharField(max_length=100)
    client_gstin = models.CharField(max_length=50)
    client_address = models.TextField()
    client_city = models.CharField(max_length=100)
    client_state = models.CharField(max_length=100)
    client_country = models.CharField(max_length=100)
    invoice = models.CharField(max_length=50)
    datetime_field1 = models.DateTimeField()
    datetime_field2 = models.DateTimeField()
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    terms_conditions = models.TextField(blank=True, null=True)


    invoice_id = models.CharField(max_length=50, blank=True, null=True, unique=True)


class Item(models.Model):
    GST_RATE_CHOICES = [
        (0, '0%'),
        (5, '5%'),
        (12, '12%'),
        (18, '18%'),
        (28, '28%'),
    ]
    
    myformdata = models.ForeignKey('MyFormData', on_delete=models.CASCADE, related_name='items')
    item_desc = models.CharField(max_length=255)
    qty = models.FloatField()
    rate = models.FloatField()
    gst_rate = models.PositiveIntegerField(choices=GST_RATE_CHOICES, default=0)
    sgst = models.FloatField(default=0.0)
    cgst = models.FloatField(default=0.0)
    cess = models.FloatField(default=0.0)




class ExpenseReport(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='expense_reports', null=True)
    company_name = models.CharField(max_length=100)
    your_name = models.CharField(max_length=100)
    company_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    report_from = models.CharField(max_length=100)
    report_to = models.CharField(max_length=100)
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()
    invoice_id = models.CharField(max_length=50, blank=True, null=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.invoice_id:
            self.invoice_id = str(uuid.uuid4())
        super().save(*args, **kwargs)

class ExpenseDetail(models.Model):
    expense_report = models.ForeignKey(ExpenseReport, on_delete=models.CASCADE, related_name='details')
    date = models.DateTimeField()
    expense_description = models.CharField(max_length=255)
    merchant = models.CharField(max_length=100)
    amount = models.FloatField()

    def __str__(self):
        return self.expense_description
    

class PackageReport(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='package_reports', null=True)
    company_name = models.CharField(max_length=100)
    your_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    client_name = models.CharField(max_length=100)
    client_city = models.CharField(max_length=100)
    client_state = models.CharField(max_length=100)
    client_country = models.CharField(max_length=100)
    package=models.CharField(max_length=100)
    order_date = models.DateTimeField()
    package_date = models.DateTimeField()
    sales_order = models.CharField(max_length=100)
    notes = models.TextField(blank=True, null=True)
    invoice_id = models.CharField(max_length=50, blank=True, null=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.invoice_id:
            self.invoice_id = str(uuid.uuid4())
        super().save(*args, **kwargs)
        
class PackageDetail(models.Model):
    package_report = models.ForeignKey(PackageReport, on_delete=models.CASCADE, related_name='details')
    item_description = models.CharField(max_length=255)
    order_quantity = models.PositiveIntegerField()
    shipped_quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.item_description