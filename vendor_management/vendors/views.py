from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Vendor, PurchaseOrder, HistoricalPerformance
from .serializers import VendorSerializer, PurchaseOrderSerializer, HistoricalPerformanceSerializer
from django.utils import timezone
from rest_framework.decorators import api_view


# Create your views here.

class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    @action(detail=True, methods=['get'])
    def performance(self, request, pk=None):
        vendor = self.get_object()
        performance_records = HistoricalPerformance.objects.filter(vendor=vendor)
        serializer = HistoricalPerformanceSerializer(performance_records, many=True)
        return Response(serializer.data)
    
    
@api_view(['POST'])
def acknowledge_purchase_order(request, po_id):
    try:
        po = PurchaseOrder.objects.get(pk=po_id)
        po.acknowledgment_date = timezone.now()

        quality_rating = request.data.get('quality_rating')
        status = request.data.get('status')
        if quality_rating is not None:
            try:
                quality_rating = float(quality_rating)
                po.quality_rating = quality_rating
            except ValueError:
                return Response({'error': 'Invalid quality rating'}, status=400)
        
        po.status = status
        po.save()
        
        return Response({'status': status, 'quality_rating': po.quality_rating})
    except PurchaseOrder.DoesNotExist:
        return Response({'error': 'Purchase Order not found'}, status=404)

class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class HistoricalPerformanceViewSet(viewsets.ModelViewSet):
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformanceSerializer