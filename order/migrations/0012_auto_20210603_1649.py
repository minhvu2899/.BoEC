# Generated by Django 3.1.7 on 2021-06-03 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0011_auto_20210603_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Chờ xác nhận', 'Chờ xác nhận'), ('Chờ lấy hàng', 'Chờ lấy hàng'), ('Đang vận chuyển', 'Đang vận chuyển'), ('Đang giao hàng', 'Đang giao hàng'), ('Đã hoàn thành', 'Đã hoàn thành'), ('Đã hủy', 'Đã hủy')], default=('Chờ xác nhận', 'Chờ xác nhận'), max_length=20),
        ),
    ]