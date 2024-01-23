# Generated by Django 5.0 on 2024-01-17 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_cars_car_type_cars_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carspecification',
            name='horsepower',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='carspecification',
            name='torque',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
