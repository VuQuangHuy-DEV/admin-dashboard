# Generated by Django 4.2.3 on 2023-11-10 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bidding', '0005_proposal_license_plate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proposal',
            old_name='bookingPost',
            new_name='booking_post',
        ),
    ]