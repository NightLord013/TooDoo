# Generated by Django 3.2.5 on 2021-08-05 14:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NoteBoardApp', '0003_auto_20210802_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='deadline',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 8, 5, 17, 12, 14), null=True, verbose_name='Дата и время выполнения'),
        ),
    ]
