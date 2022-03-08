from rest_framework import serializers
from api.models import Product, SalesInvoice, SalesInvoiceDetails

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = "__all__"

class SalesInvoiceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SalesInvoice
        fields = "__all__"

class SalesInvoiceDetailsSerializer(serializers.ModelSerializer):
    SalesInvoiceId = SalesInvoiceSerializer(many = True, read_only = True)
    ProductId = ProductSerializer(many = True, read_only = True)
    
    class Meta:
        model = SalesInvoiceDetails
        fields = "__all__"