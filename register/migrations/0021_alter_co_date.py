# Generated by Django 4.0.4 on 2022-10-30 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0020_co'),
    ]

    operations = [
        migrations.AlterField(
            model_name='co',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
