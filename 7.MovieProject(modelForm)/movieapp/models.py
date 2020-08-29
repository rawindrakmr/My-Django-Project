from django.db import models

# Create your models here.
class Movie(models.Model):
    rdate=models.DateField()
    movieName=models.CharField(max_length=60)
    hero=models.CharField(max_length=60)
    heroine=models.CharField(max_length=60)
    rating=models.IntegerField()

    def __str__(self):
        return self.movieName
