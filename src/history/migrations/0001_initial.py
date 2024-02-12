# Generated by Django 4.2.9 on 2024-02-12 17:31

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('car', '0001_initial'),
        ('vendor', '0001_initial'),
        ('customer', '0001_initial'),
        ('dealer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DealerVendorHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('price', models.PositiveIntegerField(default=0)),
                ('discount', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.car')),
                ('dealer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dealer_vendor_history', to='dealer.dealer')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vendor_dealer_history', to='vendor.vendor')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CustomerDealerHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('price', models.PositiveIntegerField(default=0)),
                ('discount', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.car')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_dealer_history', to='customer.customer')),
                ('dealer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dealer_customer_history', to='dealer.dealer')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
