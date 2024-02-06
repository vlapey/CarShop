import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    "add-cars-every-three-minutes": {
        "task": "src.cars.tasks.car_task",
        "schedule": crontab(minute="*/3"),
    },
    "buy-dealer-vendor-every-one-minute": {
        "task": "src.showroom.tasks.showroom_task",
        "schedule": crontab(minute="*/1"),
    },
    "buy-customer-dealer-every-two-minutes": {
        "task": "src.customer.tasks.customer_task",
        "schedule": crontab(minute="*/2"),
    },
}
