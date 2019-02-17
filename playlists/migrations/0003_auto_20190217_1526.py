# Generated by Django 2.1.5 on 2019-02-17 06:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('playlists', '0002_playlist_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='playlist',
            name='comments',
            field=models.ManyToManyField(related_name='comments', through='playlists.Comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='playlist',
            name='scrap',
            field=models.ManyToManyField(related_name='scrap', through='playlists.Scrap', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='scrap',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scrap_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
