# Generated by Django 2.1.7 on 2019-03-10 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_profile_loaction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='loaction',
        ),
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.CharField(default='My location default', max_length=120),
        ),
    ]