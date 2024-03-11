import pytest

from .tasks import vendor_task
from src.car.models import Car


@pytest.mark.django_db
def test_vendor_task():
    car_objects_counter = Car.objects.count()
    vendor_task()
    assert car_objects_counter == Car.objects.count()

