import pytest

from src.dealer.models import Dealer
from .tasks import dealer_task
from core.car_service import CarFinder
from src.vendor.models import Vendor
from src.car.models import Car
from src.history.models import DealerVendorHistory


@pytest.mark.django_db
def test_dealer_task():
    dealer = Dealer.objects.create(name='Dealer1', location='AE', balance=1000)
    vendor = Vendor.objects.create(name='Vendor1', foundation_year=1900, buyers_amount=500)

    car = Car.objects.create(
        brand='BMW',
        model='X5',
        engine='diesel',
        horsepower=400,
        torque=500,
        price=500,
        vendor=vendor,
    )
    car.save()

    def mock_find_cheapest_car_and_discount(dealer_or_customer):
        return [car, 10]

    CarFinder.find_cheapest_car_and_discount = mock_find_cheapest_car_and_discount

    dealer_task()

    dealer.refresh_from_db()
    car.refresh_from_db()

    assert dealer.balance == 500
    assert car.dealer == dealer
    assert car.vendor is None
    assert DealerVendorHistory.objects.filter(dealer=dealer, vendor=vendor, car=car).exists()
