# Generated by Django 2.2.8 on 2020-02-10 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0025_custompurchase_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custompurchase',
            name='status',
            field=models.CharField(blank=True, choices=[('awaiting', 'В обработке'), ('confirmed', 'Подтвержден'), ('done', 'Готов')], default='awaiting', max_length=10, null=True),
        ),
    ]