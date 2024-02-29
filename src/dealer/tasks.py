from django.utils import timezone

from src.car.models import Car
from core.car_randomizer import SpecsRandomizer
from src.dealer.models import Dealer
from celery import shared_task
from src.loyalties.models import VendorsLoyalties


def get_active_discount(cars):
    today = timezone.now()
    has_discount = VendorsLoyalties.objects.filter(
        car__in=cars,
        vendor__in=[car.vendor for car in cars],
        end_date__gte=today
    )
    if not has_discount:
        return 0

    vendor_loyal = has_discount.order_by('-discount').first()
    return vendor_loyal.discount


def get_cars_by_filters(wanted_car_specs, wanted_car_types):

    cars = Car.objects.filter(engine=wanted_car_specs.engine)

    after_filter_cars = cars.filter(horsepower__lte=wanted_car_specs.horsepower)
    if not after_filter_cars:
        cars = cars.filter(horsepower__gte=wanted_car_specs.horsepower)
    else:
        cars = after_filter_cars
    del after_filter_cars

    counter = 0
    while not cars or counter < 2:
        cars = cars.filter(car_type__in=wanted_car_types)
        counter += 1

    after_filter_cars = cars.filter(mileage__lte=wanted_car_specs.mileage)
    if not after_filter_cars:
        cars = cars.filter(mileage__gte=wanted_car_specs.mileage)
    else:
        cars = after_filter_cars
    del after_filter_cars

    after_filter_cars = cars.filter(price__lte=wanted_car_specs.price).order_by('price')
    if not after_filter_cars:
        cars = cars.filter(price__gte=wanted_car_specs.price).order_by('price')
    else:
        cars = after_filter_cars
    del after_filter_cars

    return cars


def find_cheapest_car_with_discount(discount, cars):
    discounted_prices = []
    for car in cars:
        discounted_price = car.price - car.price * (discount / 100)
        discounted_prices.append(discounted_price)
    cheapest_index = discounted_prices.index(min(discounted_prices))
    cheapest_car = cars[cheapest_index]
    return cheapest_car


def dealer_buys_car(car, dealer):
    if dealer.balance >= car.price:
        car.vendor = None  # Set vendor field to NULL
        car.dealer = dealer
        dealer.balance = dealer.balance - car.price
        dealer.save()
        car.save()
    else:
        print("dealer has insufficient balance")


@shared_task
def dealer_task():
    dealer = Dealer.objects.order_by('?').first()
    wanted_car_specs = SpecsRandomizer.randomize_specs()
    wanted_car_types = SpecsRandomizer.get_random_type()
    cars = get_cars_by_filters(wanted_car_specs, wanted_car_types)
    if not cars:
        print("No cars found with such filters")
        return

    discount = get_active_discount(cars)
    car = find_cheapest_car_with_discount(discount, cars)

    dealer_buys_car(car, dealer)
