# Generated by Django 4.2.7 on 2023-11-17 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prediction_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinput',
            name='first_name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='userinput',
            name='last_name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
