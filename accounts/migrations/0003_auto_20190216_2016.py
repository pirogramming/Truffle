# Generated by Django 2.1.5 on 2019-02-16 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlists', '0002_playlist_created_at'),
        ('accounts', '0002_auto_20190215_0620'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='scrap_playlist',
            field=models.ManyToManyField(to='playlists.PlayList'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(default='default_profile.png', upload_to='accounts/media'),
        ),
    ]
