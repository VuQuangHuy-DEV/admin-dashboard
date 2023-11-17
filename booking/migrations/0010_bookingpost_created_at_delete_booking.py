# Generated by Django 4.2.3 on 2023-11-07 00:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0009_bookingpost_bidders_bookingpost_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingpost',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='booking',
        ),
    ]
