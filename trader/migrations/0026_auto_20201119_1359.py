# Generated by Django 3.0 on 2020-11-19 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trader', '0025_auto_20201119_0630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='dealday',
            field=models.CharField(blank=True, default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='dealplace',
            field=models.CharField(blank=True, default='', max_length=999),
        ),
        migrations.AlterField(
            model_name='product',
            name='dealtime',
            field=models.CharField(blank=True, default='', max_length=5),
        ),
    ]
