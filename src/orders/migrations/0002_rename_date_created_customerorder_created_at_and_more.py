# Generated by Django 4.2.9 on 2024-01-29 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customerorder',
            old_name='date_created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='customerorder',
            old_name='date_updated',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='dealerorder',
            old_name='date_created',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='dealerorder',
            old_name='date_updated',
            new_name='updated_at',
        ),
    ]
