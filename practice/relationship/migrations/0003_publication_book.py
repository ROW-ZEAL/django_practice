# Generated by Django 4.0.6 on 2022-07-18 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relationship', '0002_bikes_owner_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=100)),
                ('publications', models.ManyToManyField(to='relationship.publication')),
            ],
            options={
                'ordering': ['headline'],
            },
        ),
    ]
