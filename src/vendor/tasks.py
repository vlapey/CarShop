from core.car_randomizer import CarRandomizer
from src.car.models import Car
from src.vendor.models import Vendor
from celery import shared_task


@shared_task
def vendor_task():
    car = Car.objects.create(CarRandomizer.randomize_car())
    random_vendor = Vendor.objects.order_by('?').first()
    car.vendor = random_vendor
    car.save()
    return car
