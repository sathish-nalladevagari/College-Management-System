# Generated by Django 4.0.4 on 2022-10-15 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0015_keys_delete_key'),
    ]

    operations = [
        migrations.CreateModel(
            name='doubt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_id', models.CharField(max_length=6)),
                ('subject', models.CharField(max_length=25)),
                ('doubt', models.CharField(max_length=90)),
                ('student', models.CharField(max_length=20)),
            ],
        ),
    ]
