# Generated by Django 3.1.3 on 2020-12-01 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0002_auto_20201201_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='credito',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
