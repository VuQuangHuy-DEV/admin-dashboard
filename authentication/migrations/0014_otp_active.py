# Generated by Django 4.2.3 on 2023-11-09 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0013_otp_log'),
    ]

    operations = [
        migrations.AddField(
            model_name='otp',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]