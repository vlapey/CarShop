import random

from celery import shared_task
from src.cars.models import Cars, CarSpecification
from core.car_randomizer import CarRandomizer


@shared_task
def car_task():
    horsepower = random.randint(150, 500)
    torque = random.randint(100, 400)
    mileage = random.randint(0, 10000)
    price = random.randint(2000, 100000)
    car_specification = CarSpecification.objects.create(
        brand=CarRandomizer.get_random_brand(),
        model=CarRandomizer.get_random_model(),
        engine=CarRandomizer.get_random_engine_type(),
        horsepower=horsepower,
        torque=torque,
        car_type=CarRandomizer.get_random_type()
    )
    car = Cars.objects.create(
        specification=car_specification,
        color=CarRandomizer.get_random_color(),
        mileage=mileage,
        price=price
    )
