# Generated by Django 2.0 on 2017-12-14 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='is_verified',
            field=models.BooleanField(default=True, verbose_name='verified'),
        ),
    ]
