# Generated by Django 3.0 on 2020-11-09 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trader', '0004_product_p_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='p_price',
            field=models.CharField(default=0, max_length=6),
        ),
    ]
