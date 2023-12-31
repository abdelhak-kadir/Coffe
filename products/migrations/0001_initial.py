# Generated by Django 4.1.7 on 2023-04-19 16:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desciption', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('is_active', models.BooleanField(default=True)),
                ('pubish_date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
