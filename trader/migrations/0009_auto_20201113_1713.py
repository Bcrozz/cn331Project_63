# Generated by Django 3.0 on 2020-11-13 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trader', '0008_auto_20201112_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='place',
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AddField(
            model_name='product',
            name='place1',
            field=models.CharField(blank=True, max_length=99),
        ),
        migrations.AddField(
            model_name='product',
            name='place2',
            field=models.CharField(blank=True, max_length=99),
        ),
    ]
