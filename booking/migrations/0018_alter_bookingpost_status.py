# Generated by Django 4.2.3 on 2023-11-10 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0017_remove_bookingpost_bidders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingpost',
            name='status',
            field=models.CharField(choices=[('waiting', 'Chờ báo giá'), ('cancel', 'Hủy bỏ'), ('approved', 'Đã xác nhận')], default='new', max_length=20),
        ),
    ]
