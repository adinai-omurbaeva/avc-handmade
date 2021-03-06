# Generated by Django 2.2.8 on 2020-02-06 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.PositiveIntegerField()),
                ('status', models.CharField(choices=[('awaiting', 'Awaiting'), ('confirmed', 'Confirmed'), ('done', 'Done')], default='draft', max_length=10)),
                ('rate', models.PositiveIntegerField(null=True)),
            ],
            options={
                'ordering': ('-price',),
            },
        ),
    ]
