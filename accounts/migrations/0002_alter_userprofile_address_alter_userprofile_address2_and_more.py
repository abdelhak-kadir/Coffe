# Generated by Django 4.1.7 on 2023-04-23 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='address2',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='city',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='code',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='state',
            field=models.CharField(max_length=100),
        ),
    ]
