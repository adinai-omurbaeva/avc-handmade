# Generated by Django 2.2.8 on 2020-02-17 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0026_auto_20200210_0442'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
