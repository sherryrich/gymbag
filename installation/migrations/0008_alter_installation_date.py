# Generated by Django 3.2.14 on 2022-10-27 13:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('installation', '0007_alter_installation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='installation',
            name='date',
            field=models.DateField(default=datetime.date(2022, 10, 27)),
        ),
    ]
