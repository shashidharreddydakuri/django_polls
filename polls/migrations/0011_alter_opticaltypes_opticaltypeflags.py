# Generated by Django 3.2.7 on 2021-09-28 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_auto_20210928_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opticaltypes',
            name='opticaltypeflags',
            field=models.ManyToManyField(to='polls.OpticalTypeFlag'),
        ),
    ]
