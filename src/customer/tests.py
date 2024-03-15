import pytest

from core.car_service import CarFinder
from src.car.models import Car
from src.customer.models import Customer
from src.customer.tasks import customer_task
from src.dealer.models import Dealer
from src.history.models import CustomerDealerHistory


@pytest.mark.django_db
def test_customer_creation():
    customer = Customer.objects.create(name='Customer1', last_name='Ferguson', balance=1000)
    dealer = Dealer.objects.create(name='Dealer1', location='AE')

    car = Car.objects.create(
        brand='BMW',
        model='X5',
        engine='diesel',
        horsepower=400,
        torque=500,
        price=500,
        dealer=dealer,
    )
    car.save()

    def mock_find_cheapest_car_and_discount(dealer_or_customer):
        return [car, 10]

    CarFinder.find_cheapest_car_and_discount = mock_find_cheapest_car_and_discount

    customer_task()

    customer.refresh_from_db()
    car.refresh_from_db()

    assert customer.balance == 500
    assert car.customer == customer
    assert car.dealer is None
    assert CustomerDealerHistory.objects.filter(dealer=dealer, customer=customer, car=car).exists()
