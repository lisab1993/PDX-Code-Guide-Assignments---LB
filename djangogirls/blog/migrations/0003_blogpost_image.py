# Generated by Django 3.1.6 on 2021-02-19 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210216_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
