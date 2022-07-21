# Generated by Django 4.0.6 on 2022-07-18 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('car_chose', models.CharField(choices=[('M', 'Mercedes-Benz'), ('T', 'Tesla'), ('L', 'Lamborghini')], max_length=1)),
            ],
        ),
    ]
