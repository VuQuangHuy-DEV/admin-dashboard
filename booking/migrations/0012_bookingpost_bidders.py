# Generated by Django 4.2.3 on 2023-11-07 00:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booking', '0011_remove_bookingpost_bidders'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingpost',
            name='bidders',
            field=models.ManyToManyField(null=True, related_name='bid_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
