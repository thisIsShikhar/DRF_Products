from rest_framework import viewsets,status
from . import models
from . import serializers
from app.restmsg import Msg
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from django.shortcuts import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination
from django.core.paginator import Paginator
from api.pagination import CustomPagination


class ProductViewset(viewsets.ViewSet):
    queryset=models.Product.objects.all()
    serializer_class=serializers.ProductSerializer
    # pagination_class = PageNumberPagination
    # pagination_class = LimitOffsetPagination
    pagination_class = CustomPagination
    
    def list(self, request, *args, **kwargs):
        queryset = models.Product.objects.all()
        # pagination_class = PageNumberPagination

        # page_number = self.request.query_params.get('page_number')
        # page_size = self.request.query_params.get('page_size ')

        # paginator = PageNumberPagination()
        # paginator = LimitOffsetPagination()
        paginator = CustomPagination()
        result_page = paginator.paginate_queryset(queryset,request, view=self)

        # paginator = Paginator(queryset, page_size)
        # serializer = serializers.ProductSerializer(paginator.page(page_number), many=True, context={'request': request})
        serializer = serializers.ProductSerializer(result_page, many=True, context={'request': request})
        return Response(
            Msg.encode(200, 'List of Products', None, serializer.data)
            , status=status.HTTP_200_OK
    )

    def create(self, request,*args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                Msg.encode(201, "Created successfully", None, serializer.data)
                , status=status.HTTP_201_CREATED
            )
        return Response(
            Msg.encode(400, None, serializer.errors, None)
            , status=status.HTTP_400_BAD_REQUEST
        )

    def retrieve(self, request, pk=None, *args, **kwargs):
        queryset = models.Product.objects.all()
        instance = get_object_or_404(queryset, pk=pk)

        serializer = serializers.ProductSerializer(instance, context={'request': request})
        return Response(
            Msg.encode(200, "Successful!", None, serializer.data)
            , status=status.HTTP_200_OK
        )

    def update(self, request, pk=None, *args, **kwargs):
        queryset = models.Product.objects.all()
        instance = get_object_or_404(queryset, pk=pk)
        
        serializer = serializers.ProductSerializer(instance, partial=True, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                Msg.encode(200, "Updated Successfully!", None, serializer.data)
                , status=status.HTTP_200_OK
            )
        return Response(
            Msg.encode(400, None, serializer.errors, None)
            ,status=status.HTTP_400_BAD_REQUEST
        )

    def destroy(self, request, pk=None, *args, **kwargs):
        queryset = models.Product.objects.all()
        instance = get_object_or_404(queryset, pk=pk)

        instance.delete()
        return Response(
            Msg.encode(200, "Deleted Successfully!", None, None)
            , status=status.HTTP_200_OK
        ) 

class SalesInvoiceViewset(viewsets.ViewSet):
    queryset=models.SalesInvoice.objects.all()
    serializer_class=serializers.SalesInvoiceSerializer
    
    def list(self, request, *args, **kwargs):
        queryset = models.SalesInvoice.objects.all()
        serializer = serializers.SalesInvoiceSerializer(queryset, many=True, context={'request': request})
        return Response(
            Msg.encode(200, 'List of SalesInvoice', None, serializer.data)
            , status=status.HTTP_200_OK
    )

    def create(self, request,*args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                Msg.encode(201, "Created successfully", None, serializer.data)
                , status=status.HTTP_201_CREATED
            )
        return Response(
            Msg.encode(400, None, serializer.errors, None)
            , status=status.HTTP_400_BAD_REQUEST
        )

    def retrieve(self, request, pk=None, *args, **kwargs):
        queryset = models.SalesInvoice.objects.all()
        instance = get_object_or_404(queryset, pk=pk)

        serializer = serializers.SalesInvoiceSerializer(instance, context={'request': request})
        return Response(
            Msg.encode(200, "Successful!", None, serializer.data)
            , status=status.HTTP_200_OK
        )

    def update(self, request, pk=None, *args, **kwargs):
        queryset = models.SalesInvoice.objects.all()
        instance = get_object_or_404(queryset, pk=pk)
        
        serializer = serializers.SalesInvoiceSerializer(instance, partial=True, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                Msg.encode(200, "Updated Successfully!", None, serializer.data)
                , status=status.HTTP_200_OK
            )
        return Response(
            Msg.encode(400, None, serializer.errors, None)
            ,status=status.HTTP_400_BAD_REQUEST
        )

    def destroy(self, request, pk=None, *args, **kwargs):
        queryset = models.SalesInvoice.objects.all()
        instance = get_object_or_404(queryset, pk=pk)

        instance.delete()
        return Response(
            Msg.encode(200, "Deleted Successfully!", None, None)
            , status=status.HTTP_200_OK
        ) 

class SalesInvoiceDetailsViewset(viewsets.ViewSet):
    queryset=models.SalesInvoiceDetails.objects.all()
    serializer_class=serializers.SalesInvoiceDetailsSerializer
    
    def list(self, request, *args, **kwargs):
        queryset = models.SalesInvoiceDetails.objects.all()
        serializer = serializers.SalesInvoiceDetailsSerializer(queryset, many=True, context={'request': request})
        return Response(
            Msg.encode(200, 'List of Sales Invoice Details', None, serializer.data)
            , status=status.HTTP_200_OK
    )

    def create(self, request,*args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                Msg.encode(201, "Created successfully", None, serializer.data)
                , status=status.HTTP_201_CREATED
            )
        return Response(
            Msg.encode(400, None, serializer.errors, None)
            , status=status.HTTP_400_BAD_REQUEST
        )

    def retrieve(self, request, pk=None, *args, **kwargs):
        queryset = models.SalesInvoiceDetails.objects.all()
        instance = get_object_or_404(queryset, pk=pk)

        serializer = serializers.SalesInvoiceDetailsSerializer(instance, context={'request': request})
        return Response(
            Msg.encode(200, "Successful!", None, serializer.data)
            , status=status.HTTP_200_OK
        )

    def update(self, request, pk=None, *args, **kwargs):
        queryset = models.SalesInvoiceDetails.objects.all()
        instance = get_object_or_404(queryset, pk=pk)
        
        serializer = serializers.SalesInvoiceDetailsSerializer(instance, partial=True, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                Msg.encode(200, "Updated Successfully!", None, serializer.data)
                , status=status.HTTP_200_OK
            )
        return Response(
            Msg.encode(400, None, serializer.errors, None)
            ,status=status.HTTP_400_BAD_REQUEST
        )

    def destroy(self, request, pk=None, *args, **kwargs):
        queryset = models.SalesInvoiceDetails.objects.all()
        instance = get_object_or_404(queryset, pk=pk)

        instance.delete()
        return Response(
            Msg.encode(200, "Deleted Successfully!", None, None)
            , status=status.HTTP_200_OK
        ) 
