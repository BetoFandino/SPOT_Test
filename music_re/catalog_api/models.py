from django.db import models


class Genres(models.Model):
    genreId = models.IntegerField(unique=False)
    name = models.CharField(max_length=100)
    url = models.URLField()


class Tracks(models.Model):

    artistName = models.CharField(max_length=100)
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    releaseDate = models.DateField()
    kind = models.CharField(max_length=100)
    artistId = models.IntegerField()
    artistUrl = models.URLField()
    contentAdvisoryRating = models.CharField(max_length=100, null=True, blank=True)
    artworkUrl100 = models.URLField()
    genres = models.ForeignKey(Genres, unique=False, on_delete=models.CASCADE)
