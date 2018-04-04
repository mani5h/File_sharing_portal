from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

VidCat = (('Comedy', 'Comedy'),
          ('Educational', 'Educational'),
          ('Horror', 'Horror'),
          ('Song', 'Song'),
          ('Movie', 'Movie'),
          ('others', 'others')
          )
AlbumCat = (('Musical ', 'Musical '),
            ('Jazz', 'Jazz'),
            ('Folk', 'Folk'),
            ('Hardcore', 'Hardcore'),
            ('Blues', 'Blues'),
            ('Rapping', 'Rapping')
            )


class Notification(models.Model):
    body = models.CharField(max_length=1000)
    sender = models.CharField(max_length=300, blank=True)
    send_to = models.ForeignKey(User, default=1)

    def __str__(self):
        return str(self.body)+" - by "+self.sender


class Message(models.Model):
    message = models.CharField(max_length=1000)
    sender = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return str(self.message)+" - by "+self.sender




class Video(models.Model):
    description = models.CharField(max_length=255)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=VidCat)
    video = models.FileField(upload_to='videos/', blank=True)
    extension = models.CharField(blank=True, max_length=10, default="mp4")
    size = models.IntegerField(blank=True, default=0)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("webapp:vid", kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Album(models.Model):
    artist = models.CharField(max_length=255)
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=20, choices=AlbumCat)
    logo = models.ImageField(upload_to='albumlogos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Song(models.Model):
    name = models.CharField(max_length=200)
    album_i = models.ForeignKey(Album, on_delete=models.CASCADE)
    song = models.FileField(upload_to='song/')
    extension = models.CharField(max_length=10, blank=True)
    size = models.BigIntegerField(blank=True, default=0)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    img = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=200)
    extension = models.CharField(max_length=10)
    size = models.BigIntegerField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class File(models.Model):
    src = models.FileField(upload_to='files/')
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=255, blank=True)
    extension = models.CharField(max_length=10)
    size = models.BigIntegerField(blank=True, default=0)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
