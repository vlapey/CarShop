# Generated by Django 4.2.9 on 2024-01-30 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('customer', 'CUSTOMER'), ('vendor', 'VENDOR'), ('dealer', 'DEALER')], default='customer'),
        ),
    ]
