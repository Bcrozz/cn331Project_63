# Generated by Django 3.0 on 2020-11-13 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trader', '0009_auto_20201113_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='p_image',
            field=models.ImageField(default='dafault1.jpg', upload_to='product_pics'),
        ),
    ]
