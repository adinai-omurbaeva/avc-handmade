# Generated by Django 2.2.8 on 2020-02-08 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_auto_20200208_0518'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='date',
            field=models.DateTimeField(null=True),
        ),
    ]
