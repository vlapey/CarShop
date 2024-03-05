from django.utils import timezone

from core.car_service import SpecsRandomizer, CarFinder
from .models import Customer
from celery import shared_task
from src.loyalties.models import DealersLoyalties
from src.history.models import CustomerDealerHistory


@shared_task
def customer_task():
    customer = Customer.objects.order_by('?').first()
    if not customer:
        print("There are no customers")
        return

    data = CarFinder.find_cheapest_car_and_discount(customer)
    car = data[0]
    discount = data[1]
    del data

    customer_buys_car(car, customer, discount)


def customer_buys_car(car, customer, discount):
    if customer.balance <= car.price:
        print("customer has insufficient balance")
        return

    record = CustomerDealerHistory(
        price=car.price,
        customer=customer,
        dealer=car.dealer,
        car=car,
        discount=discount
    )

    car.dealer = None
    car.customer = customer
    customer.balance = customer.balance - car.price
    customer.save()
    car.save()

    record.save()
