# Generated by Django 4.0.4 on 2022-10-21 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0016_doubt'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=15)),
                ('file', models.FileField(null=True, upload_to='')),
            ],
        ),
    ]
