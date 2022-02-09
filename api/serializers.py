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
    
    class Meta:
        model = SalesInvoiceDetails
        fields = "__all__"