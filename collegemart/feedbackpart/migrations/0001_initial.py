# Generated by Django 2.1.2 on 2018-11-01 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Userlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=150)),
                ('lastname', models.CharField(max_length=150)),
                ('comments', models.CharField(max_length=500)),
            ],
        ),
    ]
