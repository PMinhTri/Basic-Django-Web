# Generated by Django 4.0.4 on 2022-05-18 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baidoxe_dangki', '0002_phuongtien_thoigian'),
    ]

    operations = [
        migrations.AddField(
            model_name='phuongtien',
            name='thaydoi',
            field=models.DateTimeField(auto_now=True),
        ),
    ]