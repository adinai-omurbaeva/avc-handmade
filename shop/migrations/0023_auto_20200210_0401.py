# Generated by Django 2.2.8 on 2020-02-10 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0022_auto_20200210_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custompurchase',
            name='image1',
            field=models.ImageField(upload_to='static/images'),
        ),
        migrations.AlterField(
            model_name='custompurchase',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='static/images'),
        ),
        migrations.AlterField(
            model_name='custompurchase',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='static/images'),
        ),
    ]