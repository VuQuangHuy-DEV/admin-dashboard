# Generated by Django 4.2.3 on 2023-11-06 23:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('general', '0004_cities_division_type_alter_cities_image_url_and_more'),
        ('booking', '0006_post_booking_booking_bidder_booking_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='vehicle',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='general.vehicle'),
        ),
        migrations.AlterField(
            model_name='post_booking',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post_booking',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.vehicle'),
        ),
        migrations.DeleteModel(
            name='vehicle',
        ),
    ]