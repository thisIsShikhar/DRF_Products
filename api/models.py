from django.db import models

from django.db.models import fields
from datetime import datetime

class Product(models.Model):

    Id = models.IntegerField(primary_key=True, blank=False, null=False)
    ProductCode = models.CharField(max_length=64)
    ProductName = models.CharField(max_length=255)
    SellingPrice = models.IntegerField()
    Image = models.ImageField(blank=True, null=True)
    ImgHeight = models.CharField(max_length = 50, blank=True, null=True)
    ImgWidth = models.CharField(max_length =50, blank=True, null=True)

    # def save(self, *args, **kwargs):
    #     if self.Image != None:
    #         import cv2
    #         im = cv2.imread(self.Image)
    #         self.ImgHeight = im[0]
    #         self.ImgWidth = im[1]

    #     super(Product, self).save(*args, **kwargs)

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