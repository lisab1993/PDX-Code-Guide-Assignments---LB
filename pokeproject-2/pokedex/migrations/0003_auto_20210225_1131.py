# Generated by Django 3.1.6 on 2021-02-25 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0002_pokemon_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='image_back',
            field=models.CharField(max_length=700),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='image_front',
            field=models.CharField(max_length=700),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='types',
            field=models.CharField(max_length=700),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='url',
            field=models.CharField(default='https://pokemon.fandom.com/wiki/Pok%C3%A9mon_Wiki', max_length=700),
        ),
    ]
