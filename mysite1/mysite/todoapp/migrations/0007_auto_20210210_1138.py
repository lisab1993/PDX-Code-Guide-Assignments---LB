# Generated by Django 3.1.6 on 2021-02-10 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0006_todoitem_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
