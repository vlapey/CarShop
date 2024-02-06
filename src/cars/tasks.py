from celery import shared_task
from src.cars.models import Cars


@shared_task
def car_task():
    pass