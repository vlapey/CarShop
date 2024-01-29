# Generated by Django 4.2.9 on 2024-01-29 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0007_rename_date_created_cars_created_at_and_more'),
        ('dealer', '0002_delete_dealerscar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dealer',
            old_name='date_created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='dealer',
            old_name='date_updated',
            new_name='updated_at',
        ),
        migrations.CreateModel(
            name='DealersCar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('amount', models.IntegerField(default=0)),
                ('price', models.FloatField(default=0.0)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car_dealer_car', to='cars.cars')),
                ('dealer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dealer_dealer_car', to='dealer.dealer')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]