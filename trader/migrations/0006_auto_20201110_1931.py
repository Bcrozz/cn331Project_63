# Generated by Django 3.0 on 2020-11-10 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trader', '0005_product_p_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='p_image',
            field=models.ImageField(default='dafault1.jpg', upload_to='product_pics'),
        ),
    ]