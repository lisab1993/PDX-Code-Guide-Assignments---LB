# Generated by Django 3.1.6 on 2021-02-25 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='url',
            field=models.CharField(default='https://pokemon.fandom.com/wiki/Pok%C3%A9mon_Wiki', max_length=200),
        ),
    ]
