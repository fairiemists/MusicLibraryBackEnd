# Generated by Django 4.1.2 on 2022-10-23 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0004_alter_song_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='release_date',
            field=models.DateField(),
        ),
    ]
