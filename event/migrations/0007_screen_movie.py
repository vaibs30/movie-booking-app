# Generated by Django 3.0.8 on 2020-07-23 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0006_auto_20200723_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='screen',
            name='movie',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='movie', to='event.Movie'),
            preserve_default=False,
        ),
    ]