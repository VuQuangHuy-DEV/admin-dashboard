# Generated by Django 4.2.3 on 2023-11-09 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0016_alter_bookingpost_bidders'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookingpost',
            name='bidders',
        ),
    ]
