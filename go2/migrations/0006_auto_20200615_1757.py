# Generated by Django 3.0.7 on 2020-06-15 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('go2', '0005_auto_20200615_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='steps',
            field=models.IntegerField(default=0),
        ),
    ]
