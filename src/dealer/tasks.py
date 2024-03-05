from core.car_service import CarFinder
from src.dealer.models import Dealer
from celery import shared_task
from src.history.models import DealerVendorHistory


@shared_task
def dealer_task():
    dealer = Dealer.objects.order_by('?').first()

    if not dealer:
        print("There are no dealers")
        return

    data = CarFinder.find_cheapest_car_and_discount(dealer)

    if not data:
        print("Didn't get Data from CarFinder")
        return

    car = data[0]
    discount = data[1]
    del data

    dealer_buys_car(car, dealer, discount)


def dealer_buys_car(car, dealer, discount):
    if dealer.balance <= car.price:
        print("dealer has insufficient balance")
        return

    if not car.vendor:
        print("Car has no vendor")
        return

    record = DealerVendorHistory(
        price=car.price,
        dealer=dealer,
        vendor=car.vendor,
        car=car,
        discount=discount
    )

    car.vendor = None
    car.dealer = dealer
    dealer.balance = dealer.balance - car.price
    dealer.save()
    car.save()

    record.save()
