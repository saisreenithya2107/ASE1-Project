# Generated by Django 2.1.3 on 2018-11-16 12:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registration', '0001_initial'),
        ('seller', '0003_auto_20181116_1822'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Hostel', 'Hostel'), ('Lab', 'Lab'), ('Books', 'Books')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Products_Selling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('photo', models.ImageField(upload_to='SellingProductsPhotos')),
                ('amount', models.FloatField()),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.Category')),
                ('Seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.Profile')),
            ],
        ),
    ]
