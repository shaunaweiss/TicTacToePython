# Generated by Django 2.1.7 on 2019-04-04 23:56

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_auto_20190404_1951'),
    ]

    operations = [
        migrations.AddField(
            model_name='space',
            name='space_id',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(8)]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='board',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 4, 19, 56, 53, 774042), verbose_name='date started'),
        ),
        migrations.AlterField(
            model_name='space',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
