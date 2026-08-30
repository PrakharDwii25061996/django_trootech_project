from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/', blank=True,
        null=True
    )

    def delete(self, *args, **kwargs):
        if self.image:
            self.image.delete(save=False)
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        
        if self.pk:
            old_instance = Artist.objects.filter(id=self.pk).first()
            if (
                self.image
                and old_instance.image != self.image
            ):
                old_instance.image.delete(save=False)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ForeignKey(
    	Artist, on_delete=models.CASCADE, related_name='artist_album'
    )
    image = models.ImageField(upload_to='album/', blank=True,
        null=True
    )
    release_date = models.DateField()

    def delete(self, *args, **kwargs):
        if self.image:
            self.image.delete(save=False)
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        
        if self.pk:
            old_instance = Album.objects.filter(id=self.pk).first()
            if (
                self.image
                and old_instance.image != self.image
            ):
                old_instance.image.delete(save=False)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Track(models.Model):
    title = models.CharField(max_length=200)
    album = models.ForeignKey(
    	Album, on_delete=models.CASCADE, related_name='album_track'
    )
    image = models.ImageField(upload_to='track/',blank=True,
        null=True
    )
    order = models.PositiveIntegerField()
    duration = models.PositiveIntegerField()

    def delete(self, *args, **kwargs):
        if self.image:
            self.image.delete(save=False)
        super().delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        
        if self.pk:
            old_instance = Track.objects.filter(id=self.pk).first()
            if (
                self.image
                and old_instance.image != self.image
            ):
                old_instance.image.delete(save=False)

        super().save(*args, **kwargs)


    def __str__(self):
        return self.title
