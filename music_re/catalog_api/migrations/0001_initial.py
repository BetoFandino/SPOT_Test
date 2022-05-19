# Generated by Django 4.0.4 on 2022-05-19 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genreId', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Tracks',
            fields=[
                ('artistName', models.CharField(max_length=100)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('releaseDate', models.DateField()),
                ('kind', models.CharField(max_length=100)),
                ('artistId', models.IntegerField()),
                ('artistUrl', models.URLField()),
                ('contentAdvisoryRating', models.CharField(blank=True, max_length=100, null=True)),
                ('artworkUrl100', models.URLField()),
                ('genres', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog_api.genres')),
            ],
        ),
    ]
