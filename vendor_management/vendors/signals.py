from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now
from .models import PurchaseOrder, Vendor, HistoricalPerformance
from django.db.models import Avg, Count, Q, F


@receiver(post_save, sender=PurchaseOrder)
def update_performance_metrics(sender, instance, created, **kwargs):
    if not created and instance.status == 'COMPLETED':
        update_metrics(instance.vendor)

def update_metrics(vendor):
    # Calculate on-time delivery rate
    completed_pos = PurchaseOrder.objects.filter(vendor=vendor, status='COMPLETED')
    on_time_deliveries = completed_pos.filter(delivery_date__lte=F('order_date')).count()
    on_time_delivery_rate = (on_time_deliveries / completed_pos.count() * 100) if completed_pos.exists() else 0

    # Calculate quality rating average
    quality_ratings = completed_pos.exclude(quality_rating__isnull=True).aggregate(average=Avg('quality_rating'))
    quality_rating_avg = quality_ratings.get('average') or 0

    # Calculate average response time
    acknowledged_pos = PurchaseOrder.objects.filter(vendor=vendor, acknowledgment_date__isnull=False)
    total_response_time = sum([(po.acknowledgment_date - po.issue_date).total_seconds() for po in acknowledged_pos])
    average_response_time = (total_response_time / acknowledged_pos.count()) if acknowledged_pos.exists() else 0

    # Calculate fulfillment rate
    total_pos_count = PurchaseOrder.objects.filter(vendor=vendor).count()
    fulfilled_pos_count = completed_pos.count()
    fulfillment_rate = (fulfilled_pos_count / total_pos_count * 100) if total_pos_count > 0 else 0
    
    print("Creating.....")
    # Save the calculated metrics to the HistoricalPerformance model
    historical_performance_data = HistoricalPerformance.objects.filter(vendor=vendor)

    if len(historical_performance_data) > 0:
        historical_performance_data.update(on_time_delivery_rate=on_time_delivery_rate,
            quality_rating_avg=quality_rating_avg,
            average_response_time=average_response_time,
            fulfillment_rate=fulfillment_rate)
    else:
        HistoricalPerformance.objects.create(
            vendor=vendor,
            date=now(),
            on_time_delivery_rate=on_time_delivery_rate,
            quality_rating_avg=quality_rating_avg,
            average_response_time=average_response_time,
            fulfillment_rate=fulfillment_rate
        )
