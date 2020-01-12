from django.db import models

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=128)
    year = models.IntegerField()
    summary = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    Genre = models.ForeignKey(Genre, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name