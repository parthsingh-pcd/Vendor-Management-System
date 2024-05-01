from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import VendorViewSet, PurchaseOrderViewSet
from vendors.views import acknowledge_purchase_order


router = DefaultRouter()
router.register(r'vendors', VendorViewSet)
router.register(r'purchase_orders', PurchaseOrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('purchase_orders/<int:po_id>/acknowledge', acknowledge_purchase_order, name='purchaseorder-acknowledge'),
]
