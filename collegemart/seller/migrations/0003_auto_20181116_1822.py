# Generated by Django 2.1.3 on 2018-11-16 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0002_remove_products_selling_seller'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products_selling',
            name='Category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Products_Selling',
        ),
    ]