# Generated by Django 3.0.8 on 2020-07-23 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_auto_20200722_1533'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('rating', models.IntegerField(max_length=5)),
                ('imageURL', models.URLField(default='https://increasify.com.au/wp-content/uploads/2016/08/default-image.png')),
                ('is_showing', models.BooleanField(default=True)),
                ('is_upcoming', models.BooleanField(default=False)),
                ('cast', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Screen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('name', models.CharField(choices=[('Elite', 'Elite'), ('Royal', 'Royal'), ('Economy', 'Economy')], max_length=50)),
                ('A', models.IntegerField(default=10)),
                ('B', models.IntegerField(default=10)),
                ('C', models.IntegerField(default=10)),
                ('D', models.IntegerField(default=10)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_name', to='event.Movie')),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_organizer',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.AddField(
            model_name='movie',
            name='screens',
            field=models.ManyToManyField(related_name='screen', to='event.Screen'),
        ),
    ]
