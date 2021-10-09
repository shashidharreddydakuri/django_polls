# Generated by Django 3.2.7 on 2021-10-04 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0024_auto_20211003_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kelvin',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='opticaltypes',
            name='opticaltypeflags',
            field=models.ManyToManyField(to='polls.OpticalTypeFlag'),
        ),
    ]
