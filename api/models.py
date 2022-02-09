from django.db import models

from django.db.models import fields
from datetime import datetime

class Product(models.Model):

    Id = models.IntegerField(primary_key=True, blank=False, null=False)
    ProductCode = models.CharField(max_length=64)
    ProductName = models.CharField(max_length=255)
    SellingPrice = models.IntegerField()

class SalesInvoice(models.Model):

    Id = models.IntegerField(primary_key=True, blank=False, null= False)
    InvoiceNumber = models.CharField(max_length=64)
    InvoiceDate = models.DateField()
    CustomerName = models.CharField(max_length=255)
    TotalAmount = models.IntegerField()

class SalesInvoiceDetails(models.Model):

    Id = models.IntegerField(primary_key=True, blank=False, null= False)
    SalesInvoiceId = models.ManyToManyField(SalesInvoice)
    LineNumber = models.IntegerField()
    ProductId = models.ManyToManyField(Product)
    Productname = models.CharField(max_length=255)
    Quantity = models.IntegerField()
    UnitPrice = models.IntegerField()
    Amount = models.IntegerField()