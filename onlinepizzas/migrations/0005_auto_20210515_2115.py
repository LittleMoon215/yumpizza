# Generated by Django 3.2.3 on 2021-05-15 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinepizzas', '0004_auto_20210515_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drink',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='snack',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
