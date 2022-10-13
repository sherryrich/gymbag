# Generated by Django 3.2.14 on 2022-10-13 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='contact_reason',
            field=models.CharField(choices=[('please select', 'Please select'), ('returns', 'Returns'), ('availability', 'Availability'), ('pricing', 'Pricing'), ('feedback', 'Feedback'), ('other', 'Other')], default='please select below', max_length=24),
        ),
    ]