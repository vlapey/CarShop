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


@shared_task
def dealer_task():
    dealer = Dealer.objects.order_by('?').first()
    wanted_car_specs = SpecsRandomizer.randomize_specs()

    cars = Car.objects.filter(engine=wanted_car_specs.engine)
    cars = cars.filter(horsepower=wanted_car_specs.horsepower)
    cars = cars.filter(car_type=wanted_car_specs.car_type)
    cars = cars.filter(mileage=wanted_car_specs.mileage)
    cars = cars.filter(price=wanted_car_specs.price).order_by('price')

    discount = get_active_discount(cars)
    cheapest_car = None

    if discount:
        discounted_prices = []
        for car in cars:
            discounted_price = car.price - car.price * (discount / 100)
            discounted_prices.append(discounted_price)
        cheapest_index = discounted_prices.index(min(discounted_prices))
        cheapest_car = cars[cheapest_index]

    if cheapest_car:
        if dealer.balance >= cheapest_car.price:
            cheapest_car.vendor = None  # Set vendor field to NULL
            cheapest_car.dealer = dealer
            dealer.balance = dealer.balance - cheapest_car.price
            dealer.save()
            cheapest_car.save()
        else:
            print("dealer has insufficient balance")
    else:
        print("There's no such car")
