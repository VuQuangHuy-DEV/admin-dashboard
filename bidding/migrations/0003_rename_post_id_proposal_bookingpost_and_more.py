# Generated by Django 4.2.3 on 2023-11-09 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bidding', '0002_proposal_post_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='proposal',
            old_name='post_id',
            new_name='bookingPost',
        ),
        migrations.RemoveField(
            model_name='proposal',
            name='service',
        ),
    ]
