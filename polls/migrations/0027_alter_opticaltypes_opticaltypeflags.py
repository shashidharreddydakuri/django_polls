# Generated by Django 3.2.7 on 2021-10-04 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0026_alter_opticaltypes_opticaltypeflags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opticaltypes',
            name='opticaltypeflags',
            field=models.ManyToManyField(to='polls.OpticalTypeFlag'),
        ),
    ]