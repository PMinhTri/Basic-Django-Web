# Generated by Django 4.0.4 on 2022-05-18 15:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('baidoxe_dangki', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='phuongtien',
            name='thoigian',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 5, 18, 15, 53, 55, 33772, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
