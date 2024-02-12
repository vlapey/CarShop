from datetime import date

from src.car.models import CarSpecification
from src.dealer.models import Dealer
from celery import shared_task
from src.loyalties.models import VendorsLoyalties


@shared_task
def dealer_task():
    dealer = Dealer.objects.order_by('?').first()
    # wanted_specification = CarSpecification(
    #     brand=CarRandomizer.get_random_brand(),
    #     model=CarRandomizer.get_random_model(),
    #     engine=CarRandomizer.get_random_engine_type(),
    #     horsepower=horsepower,
    #     torque=torque,
    #     car_type=CarRandomizer.get_random_type()
    # )
    # discount = get_active_discount(car, dealer)
    # DealerVendorHistory.objects.create(
    #     car=car,
    #     price=car.price,
    #     discount=discount,
    #     dealer=dealer,
    #     vendor=
    # )
    pass


def get_active_discount(car, vendor):
    today = date.today()
    try:
        discount = VendorsLoyalties.objects.filter(start_date__lte=today, end_date__gte=today,
                                                   car=car, vendor=vendor).first()
        return discount
    except VendorsLoyalties.DoesNotExist:
        return 0


