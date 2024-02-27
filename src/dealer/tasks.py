from datetime import date

from src.car.models import Car
from core.car_randomizer import CarRandomizer
from src.dealer.models import Dealer
from celery import shared_task
from src.loyalties.models import VendorsLoyalties
from django.db.models import Exists, OuterRef
from django.db.models import Q


def get_active_discount(cars):
    today = date.today()
    has_discount = 0
    try:
        for vendor_loyal in VendorsLoyalties.objects.all():
            has_discount = VendorsLoyalties.objects.filter(
                car__in=cars,
                vendor=vendor_loyal.vendor
            )
        vendor_loyal = has_discount.order_by('price').first()
        return vendor_loyal.discount
    except VendorsLoyalties.DoesNotExist:
        return 0


@shared_task
def dealer_task():
    dealer = Dealer.objects.order_by('?').first()
    wanted_car_specs = CarRandomizer.randomize_car()

    cars = Car.objects.filter(engine=wanted_car_specs.engine)
    cars = cars.filter(horsepower__lte=wanted_car_specs.horsepower)
    cars.filter(car_type=wanted_car_specs.car_type)
    cars = cars.filter(mileage__lte=wanted_car_specs.mileage)
    cars = cars.filter(price__lte=wanted_car_specs.price).order_by('price')

    # discount = get_active_discount(cars)
    # if discount:
    #     for car in cars:
    #         car.price = car.price - cars.price * (discount / 100)

    car = cars.order_by('price').first()

    if car is not None:
        car.vendor = None  # Set vendor field to NULL
        car.dealer = dealer
        car.save()
    else:
        print("There's no such car")
