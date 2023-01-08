from django.contrib import admin
from api.models import Product, SalesInvoice, SalesInvoiceDetails
from django_summernote.admin import SummernoteModelAdmin

class ProductAdmin(SummernoteModelAdmin):
    list_display = ('Id','ProductCode','ProductName','SellingPrice')
    search_fields = ('Productname',)
    summernote_fields = ('ProductInfo',)

admin.site.register(Product, ProductAdmin)
admin.site.register(SalesInvoice)
admin.site.register(SalesInvoiceDetails)