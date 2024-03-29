# Generated by Django 3.0 on 2020-11-12 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trader', '0007_profile_faculty'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pStatus',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='faculty',
            field=models.CharField(blank=True, choices=[('E', 'Faculty of Engineering'), ('L', 'Faculty of Law'), ('AE', 'Faculty of Architecture'), ('DY', 'Faculty of Dentisty'), ('LA', 'Faculty of Liberal Art'), ('PS', 'Faculty of Political Science'), ('M', 'Faculty of Medicine'), ('EM', 'Faculty of Economics')], max_length=2),
        ),
    ]
