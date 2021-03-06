# Generated by Django 3.1.6 on 2021-02-10 18:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_todoitem_completed_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='completed_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='todoitem',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
