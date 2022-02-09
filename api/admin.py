from django.contrib import admin
from api.models import Product, SalesInvoice, SalesInvoiceDetails

admin.site.register(Product)
admin.site.register(SalesInvoice)
admin.site.register(SalesInvoiceDetails)