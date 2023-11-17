# Generated by Django 4.2.3 on 2023-11-08 15:56

from django.db import migrations, models
import functools
import ultis.helper


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0009_alter_user_back_id_image_alter_user_front_id_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='user_media/images/avatar/default.png', upload_to=functools.partial(ultis.helper.custom_user_image_path, *(), **{'path': 'avatar'})),
        ),
    ]