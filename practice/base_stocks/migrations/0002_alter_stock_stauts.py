# Generated by Django 4.0.6 on 2022-07-15 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_stocks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='Stauts',
            field=models.IntegerField(),
        ),
    ]