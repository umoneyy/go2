# Generated by Django 3.0.7 on 2020-06-13 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=400)),
                ('password', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
            ],
        ),
    ]
