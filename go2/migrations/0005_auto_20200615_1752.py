# Generated by Django 3.0.7 on 2020-06-15 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('go2', '0004_auto_20200615_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='steps',
            field=models.IntegerField(default=0, max_length=10),
        ),
    ]