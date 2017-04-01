# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-21 06:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


def split_datetime(apps, schema_editor):
    Booking = apps.get_model('opencabs', 'Booking')
    for booking in Booking.objects.all():
        booking.travel_date = booking.travel_datetime.date()
        booking.travel_time = booking.travel_datetime.time()
        booking.save()


class Migration(migrations.Migration):

    dependencies = [
        ('opencabs', '0005_booking_ssr'),
    ]

    now = datetime.datetime.now()

    operations = [
        migrations.AddField(
            model_name='booking',
            name='travel_date',
            field=models.DateField(default=now.date()),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='travel_time',
            field=models.TimeField(default=now.time()),
            preserve_default=False,
        ),
        migrations.RunPython(split_datetime),
    ]