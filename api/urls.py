from api.viewsets import ProductViewset, SalesInvoiceViewset, SalesInvoiceDetailsViewset
from rest_framework import routers
from django.urls import path,include

router = routers.DefaultRouter()
router.register('product', ProductViewset)
router.register('salesinvoice', SalesInvoiceViewset)
router.register('salesinvoicedetails', SalesInvoiceDetailsViewset)

urlpatterns = [
    path("",include(router.urls))
]