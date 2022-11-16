from api.viewsets import ProductViewset, SalesInvoiceViewset, SalesInvoiceDetailsViewset, SearchViewset
from rest_framework import routers
from django.urls import path,include

router = routers.DefaultRouter()
router.register('product', ProductViewset)
router.register('salesinvoice', SalesInvoiceViewset)
router.register('salesinvoicedetails', SalesInvoiceDetailsViewset)
router.register('search', SearchViewset, basename='search')

urlpatterns = [
    path("",include(router.urls))
]