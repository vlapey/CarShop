from core.car_randomizer import CarRandomizer
from src.vendor.models import Vendor
from celery import shared_task


@shared_task
def vendor_task():
    car = CarRandomizer.randomize_car()
    vendor = Vendor.objects.order_by('?').first()
    car.vendor = vendor
    car.save()
