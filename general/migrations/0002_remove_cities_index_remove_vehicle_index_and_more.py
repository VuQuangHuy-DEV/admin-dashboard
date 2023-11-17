# Generated by Django 4.2.3 on 2023-11-06 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cities',
            name='index',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='index',
        ),
        migrations.AddField(
            model_name='cities',
            name='order',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='order',
            field=models.IntegerField(default=1),
        ),
    ]