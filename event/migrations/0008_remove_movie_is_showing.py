# Generated by Django 3.0.8 on 2020-07-23 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0007_screen_movie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='is_showing',
        ),
    ]