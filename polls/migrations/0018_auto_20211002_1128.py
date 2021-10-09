# Generated by Django 3.2.7 on 2021-10-02 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0017_auto_20211002_1126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manufacturer',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='project',
            name='updated',
        ),
        migrations.AlterField(
            model_name='opticaltypes',
            name='opticaltypeflags',
            field=models.ManyToManyField(to='polls.OpticalTypeFlag'),
        ),
    ]