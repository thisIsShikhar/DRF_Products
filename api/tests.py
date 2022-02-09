from django.urls import reverse
from django.test import TestCase
from .models import Product
from rest_framework import status, request
from rest_framework.test import APITestCase
from api import viewsets


def createItem(client):
    url = "http://127.0.0.1:8000/api/v1/product/"
    data = {"Id": 125,
            "ProductCode": "Product3",
            "ProductName": "product3",
            "SellingPrice": 3000}
    return client.post(url, data, format='json')


class ProductCreateTest(APITestCase):

    def setUp(self):
        self.response = createItem(self.client)

    def test_received_201_created_status_code(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_item_was_created(self):
        self.assertEqual(Product.objects.count(), 1)

    def test_item_has_correct_productname(self):
        self.assertEqual(Product.objects.get().ProductName, 'product3')

    def test_item_has_correct_productcode(self):
        self.assertEqual(Product.objects.get().ProductCode, 'Product3')

    def test_item_has_correct_id(self):
        self.assertEqual(Product.objects.get().Id, 125)

    def test_item_has_correct_sellingprice(self):
        self.assertEqual(Product.objects.get().SellingPrice, 3000)


class ProductUpdateTest(APITestCase):

    def setUp(self):
        self.response = createItem(self.client)
        url = f"http://127.0.0.1:8000/api/v1/product/{Product.objects.get().Id}/"
        data = {"Id": 125,
                "ProductCode": "Product03",
                "ProductName": "product03",
                "SellingPrice": 3050}
        self.response = self.client.put(url, data, format='json')

    def test_received_200_updated_status_code(self):
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    def test_item_was_created(self):
        self.assertEqual(Product.objects.count(), 1)

    def test_item_has_correct_updated_productname(self):
        self.assertEqual(Product.objects.get().ProductName, 'product03')

    def test_item_has_correct_updated_productcode(self):
        self.assertEqual(Product.objects.get().ProductCode, 'Product03')

    def test_item_has_correct_updated_id(self):
        self.assertEqual(Product.objects.get().Id, 125)

    def test_item_has_correct_updated_sellingprice(self):
        self.assertEqual(Product.objects.get().SellingPrice, 3050)


class TestDeleteTodoItem(APITestCase):

    def setUp(self):
        response = createItem(self.client)
        # self.assertEqual(TodoItem.objects.count(), 1)
        url = f"http://127.0.0.1:8000/api/v1/product/{Product.objects.get().Id}/"
        self.response = self.client.delete(url)

    def test_received_204_no_content_status_code(self):
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    def test_the_item_was_deleted(self):
        self.assertEqual(Product.objects.count(), 0)
