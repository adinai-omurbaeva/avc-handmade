# Generated by Django 2.2.8 on 2020-02-08 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='static/images'),
        ),
    ]
