from django.db import models
from django.contrib import admin

# Create your models here.


class Movie(models.Model):
    GENRE_OPTIONS = (
        ('Horror', 'Horror'),
        ('Drama', 'Drama'),
        ('Comedy', 'Comedy'),
        ('SciFi', 'SciFi')
    )
    title = models.CharField(max_length=200)
    release = models.DateField()
    director = models.CharField(max_length=30)
    genre = models.CharField(max_length=10,
                             choices=GENRE_OPTIONS)


class ItemAdmin(admin.ModelAdmin):
    list_display = ["title"]
    search_fields = ["title"]

admin.site.register(Movie, ItemAdmin)