# Generated by Django 4.2.3 on 2023-11-07 14:33

from django.db import migrations, models
import functools
import ultis.helper


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0002_rename_branch_model_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentalpost',
            name='image_desc1',
            field=models.ImageField(default='/', upload_to=functools.partial(ultis.helper.custom_user_image_path, *(), **{'path': 'rental'})),
        ),
        migrations.AddField(
            model_name='rentalpost',
            name='image_desc2',
            field=models.ImageField(default='/', upload_to=functools.partial(ultis.helper.custom_user_image_path, *(), **{'path': 'rental'})),
        ),
        migrations.AddField(
            model_name='rentalpost',
            name='image_desc3',
            field=models.ImageField(default='/', upload_to=functools.partial(ultis.helper.custom_user_image_path, *(), **{'path': 'rental'})),
        ),
        migrations.AddField(
            model_name='rentalpost',
            name='image_desc4',
            field=models.ImageField(default='/', upload_to=functools.partial(ultis.helper.custom_user_image_path, *(), **{'path': 'rental'})),
        ),
        migrations.AddField(
            model_name='rentalpost',
            name='image_desc5',
            field=models.ImageField(default='/', upload_to=functools.partial(ultis.helper.custom_user_image_path, *(), **{'path': 'rental'})),
        ),
    ]