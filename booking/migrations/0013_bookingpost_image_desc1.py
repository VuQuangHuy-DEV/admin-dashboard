# Generated by Django 4.2.3 on 2023-11-07 14:11

from django.db import migrations, models
import functools
import ultis.helper


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0012_bookingpost_bidders'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingpost',
            name='image_desc1',
            field=models.ImageField(default='/', upload_to=functools.partial(ultis.helper.custom_user_image_path, *(), **{'path': 'booking'})),
        ),
    ]
