# Generated by Django 5.0 on 2024-01-11 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('balance', models.PositiveIntegerField(default=0)),
                ('is_having_license', models.CharField(choices=[('yes', 'y'), ('no', 'n')], default='n', max_length=3)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
