from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Vendor, PurchaseOrder
from .models import *
from django.utils import timezone

class VendorAPITests(APITestCase):

    def setUp(self):
        # Create a vendor object and save it as an attribute
        self.vendor = Vendor.objects.create(name="Vendor 1", contact_details="Contact Info", address="1234 Street", vendor_code="V001")

    def test_create_vendor(self):
        """
        Ensure we can create a new vendor object.
        """
        url = reverse('vendor-list')
        data = {'name': 'Vendor 2', 'contact_details': 'Contact Info 2', 'address': 'OU Colony Manikonda', 'vendor_code': 'V002'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Vendor.objects.get(id=1).name, 'Vendor 1')

    def test_get_vendor(self):
        """
        Ensure we can retrieve a vendor object.
        """
        url = reverse('vendor-detail', args=[self.vendor.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Vendor 1')

    def test_update_vendor(self):
        """
        Ensure we can update a vendor object.
        """
        url = reverse('vendor-detail', args=[self.vendor.id])
        data = {'name': 'Updated Vendor 1', 'contact_details': 'Contact Info', 'address': 'New Address', 'vendor_code': 'V001'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Vendor.objects.get(id=1).name, 'Updated Vendor 1')

    def test_delete_vendor(self):
        """
        Ensure we can delete a vendor object.
        """
        url = reverse('vendor-detail', args=[self.vendor.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Vendor.objects.count(), 0)

class PurchaseOrderAPITests(APITestCase):
    def setUp(self):
        self.vendor = Vendor.objects.create(name="Vendor 1", contact_details="Contact Info", address="1234 Street", vendor_code="V001")
        self.purchase_order = PurchaseOrder.objects.create(vendor=self.vendor, po_number="PO12345", order_date="2024-05-01 07:25:17.808062+00:00", delivery_date="2024-05-01 10:15:17.708052+00:00", items='{"item": "Sample Item", "quantity": 10}', quantity=10, status='PENDING')

    def test_acknowledge_purchase_order(self):
        """
        Ensure we can acknowledge a purchase order.
        """
        url = reverse('purchaseorder-acknowledge', args=[self.purchase_order.id])
        data = {'acknowledgment_date': timezone.now(), 'status':'COMPLETED'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(PurchaseOrder.objects.get(id=1).status, 'COMPLETED')

