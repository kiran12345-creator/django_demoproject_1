from django.db import models
class Movie(models.Model):



    movie_name=models.CharField(max_length=50)
    language=models.CharField(max_length=20)
    director=models.CharField(max_length=25)
    release_year=models.DateField()
    duration=models.DurationField()
    rating=models.IntegerField()


# Create your models here.
