# Generated by Django 3.2.9 on 2021-11-14 19:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('calories', '0003_alter_foodcalorie_calorie'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodcalorie',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
