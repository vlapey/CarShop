import pytest

from .tasks import vendor_task
from src.car.models import Car


@pytest.mark.django_db
def vendor_task_test():
    car_objects_counter = Car.objects.count()
    vendor_task()
    assert car_objects_counter == Car.objects.count()

