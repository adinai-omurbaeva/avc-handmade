# Generated by Django 2.2.8 on 2020-02-18 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0034_auto_20200218_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custompurchase',
            name='image2',
            field=models.ImageField(blank=True, default='no-image.png', upload_to='static/images', verbose_name='Изображение 2'),
        ),
        migrations.AlterField(
            model_name='custompurchase',
            name='image3',
            field=models.ImageField(blank=True, default='no-image.png', upload_to='static/images', verbose_name='Изображение 3'),
        ),
    ]
