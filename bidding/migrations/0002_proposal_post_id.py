# Generated by Django 4.2.3 on 2023-11-09 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0017_remove_bookingpost_bidders'),
        ('bidding', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposal',
            name='post_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='booking.bookingpost'),
        ),
    ]
