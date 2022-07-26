# Generated by Django 4.0.6 on 2022-07-18 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('relationship', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=20)),
                ('shop_name', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Owner_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('bike_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='relationship.bikes')),
            ],
            options={
                'ordering': ['bike_details'],
            },
        ),
    ]
