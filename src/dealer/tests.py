import pytest

from core.car_service import CarFinder
from src.dealer.models import Dealer
from .tasks import dealer_task
from src.car.models import Car
from src.vendor.models import Vendor


@pytest.fixture
def create_dealer():
    def _create_dealer(balance):
        dealer = Dealer.objects.create(name='Dealer1', balance=balance, location="AE")
        return dealer
    return _create_dealer


@pytest.fixture
def create_car():
    def _create_car(price):
        car_vendor = Vendor.objects.create(name='Vendor1', foundation_year=1900, buyers_amount=500)
        car = Car.objects.create(name='Car1', price=price, vendor=car_vendor)
        return car
    return _create_car


def mock_car_finder(monkeypatch):
    class MockCarFinder:
        @staticmethod
        def find_cheapest_car_and_discount(dealer_or_customer):
            car = Car(price=5000)
            discount = 10
            return [car, discount]

    monkeypatch.setattr(CarFinder, 'find_cheapest_car_and_discount', MockCarFinder.find_cheapest_car_and_discount)


@pytest.mark.django_db
def test_dealer_task(create_dealer, create_car, mock_car_finder):
    dealer = create_dealer(balance=10000)
    car = create_car(price=5000)

    dealer_task()

    updated_dealer = Dealer.objects.get(id=dealer.id)
    updated_car = Car.objects.get(id=car.id)

    assert updated_dealer.balance == 5000
    assert updated_car.dealer == dealer
    assert updated_car.vendor is None
