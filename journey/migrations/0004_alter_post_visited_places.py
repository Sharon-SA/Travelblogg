# Generated by Django 4.0.1 on 2022-02-15 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journey', '0003_alter_post_favorite_place_alter_post_visited_places'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='visited_places',
            field=models.CharField(max_length=100),
        ),
    ]
