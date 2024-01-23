# Generated by Django 5.0 on 2024-01-12 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='car_type',
            field=models.CharField(choices=[('Sedan', 'sedan'), ('Coupe', 'coupe'), ('Hatchback', 'hatchback'), ('Minivan', 'minivan'), ('Electric', 'electric')], default='sedan', max_length=20),
        ),
        migrations.AddField(
            model_name='cars',
            name='color',
            field=models.CharField(choices=[('Red', 'red'), ('Blue', 'blue'), ('Yellow', 'yellow'), ('Green', 'green'), ('Black', 'black'), ('White', 'white'), ('Cyan', 'cyan')], default='black', max_length=10),
        ),
    ]
