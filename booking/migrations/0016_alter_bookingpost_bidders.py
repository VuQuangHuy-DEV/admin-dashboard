# Generated by Django 4.2.3 on 2023-11-09 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bidding', '0001_initial'),
        ('booking', '0015_remove_bookingpost_image_desc1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingpost',
            name='bidders',
            field=models.ManyToManyField(null=True, related_name='bid_posts', to='bidding.proposal'),
        ),
    ]
