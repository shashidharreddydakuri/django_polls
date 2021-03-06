# Generated by Django 3.2.7 on 2021-10-02 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0020_auto_20211002_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='material',
            name='Description',
            field=models.TextField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='opticaltypes',
            name='opticaltypeflags',
            field=models.ManyToManyField(to='polls.OpticalTypeFlag'),
        ),
    ]
