# Generated by Django 2.1.5 on 2019-02-11 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20190211_0554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='media/default_profile.png', upload_to='accounts/media'),
        ),
    ]