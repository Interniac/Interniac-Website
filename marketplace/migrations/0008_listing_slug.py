# Generated by Django 3.1.6 on 2021-02-21 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0007_auto_20210221_0008'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
