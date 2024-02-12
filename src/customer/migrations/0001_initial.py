# Generated by Django 4.2.9 on 2024-02-12 17:31

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
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
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
