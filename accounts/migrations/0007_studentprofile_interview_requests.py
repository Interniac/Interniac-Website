# Generated by Django 3.1.6 on 2021-03-07 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0009_auto_20210307_0053'),
        ('accounts', '0006_auto_20210307_0053'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='interview_requests',
            field=models.ManyToManyField(related_name='student_interview_requests', to='marketplace.Listing'),
        ),
    ]
