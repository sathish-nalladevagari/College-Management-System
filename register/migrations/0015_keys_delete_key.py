# Generated by Django 4.0.4 on 2022-09-30 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0014_delete_form'),
    ]

    operations = [
        migrations.CreateModel(
            name='keys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch', models.TextField(choices=[('CSE', 'COMPUTER SCIENCE AND ENGINEERING'), ('CIV', 'CIVIL ENGINEERING'), ('MECH', 'MECHANICAL ENGINEERING'), ('ECE', 'ELECTRONICS AND COMMUNICATION ENGINEERING'), ('EEE', 'ELECTRICAL AND ELECTRONIC ENGINEERING')])),
                ('year', models.CharField(choices=[('I', 'I ST YEAR'), ('II', 'II ND YEAR'), ('III', 'III RD YEAR'), ('IV', 'IV TH YEAR')], max_length=6)),
                ('regulation', models.CharField(choices=[('r19', 'r19'), ('r20', 'r20'), ('r21', 'r21'), ('r22', 'r22')], max_length=6)),
                ('subject', models.CharField(max_length=35)),
                ('key', models.CharField(max_length=6)),
            ],
        ),
        migrations.DeleteModel(
            name='key',
        ),
    ]
