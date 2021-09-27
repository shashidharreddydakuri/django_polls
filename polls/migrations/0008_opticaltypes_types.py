# Generated by Django 3.2.7 on 2021-09-27 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_opticaltypes_opticaltypeflags'),
    ]

    operations = [
        migrations.AddField(
            model_name='opticaltypes',
            name='types',
            field=models.CharField(blank=True, choices=[('1', 'yellow'), ('2', 'red'), ('3', 'black')], max_length=32, null=True),
        ),
    ]
