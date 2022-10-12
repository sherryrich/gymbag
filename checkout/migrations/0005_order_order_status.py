# Generated by Django 3.2.14 on 2022-10-12 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_order_user_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('CON', 'Confirmed'), ('SHIP', 'Shipped'), ('CAN', 'Cancelled')], default='CON', max_length=10),
        ),
    ]
