# Generated by Django 4.1.7 on 2023-04-23 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_options'),
        ('accounts', '0002_alter_userprofile_address_alter_userprofile_address2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='product_fav',
            field=models.ManyToManyField(to='products.product'),
        ),
    ]
