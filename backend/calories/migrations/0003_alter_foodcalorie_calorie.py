# Generated by Django 3.2.9 on 2021-11-12 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calories', '0002_foodcalorie_is_inactive'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodcalorie',
            name='calorie',
            field=models.PositiveIntegerField(),
        ),
    ]
