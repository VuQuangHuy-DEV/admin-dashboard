# Generated by Django 4.2.3 on 2023-11-06 23:52

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('general', '0004_cities_division_type_alter_cities_image_url_and_more'),
        ('booking', '0007_alter_booking_vehicle_alter_post_booking_user_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='post_booking',
            new_name='BookingPost',
        ),
    ]
