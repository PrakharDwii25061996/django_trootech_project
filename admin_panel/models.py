from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(
    	Artist, on_delete=models.CASCADE, related_name='artist_album'
    )
    release_date = models.DateField()

    def __str__(self):
        return self.title


class Track(models.Model):
    title = models.CharField(max_length=200)
    album = models.ForeignKey(
    	Album, on_delete=models.CASCADE, related_name='album_track'
    )
    order = models.PositiveIntegerField()
    duration = models.PositiveIntegerField()

    def __str__(self):
        return self.title
