# Generated by Django 3.0.7 on 2021-05-05 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlinepizzas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=50, unique=True)),
                ('number_of_vacancy', models.IntegerField()),
                ('payment', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Workers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50)),
                ('birthday', models.DateField()),
                ('employment_date', models.DateField()),
                ('number', models.CharField(db_index=True, max_length=12, unique=True)),
                ('employment_history_number', models.CharField(max_length=30)),
                ('email', models.EmailField(db_index=True, max_length=254, unique=True)),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinepizzas.Position')),
            ],
        ),
    ]
