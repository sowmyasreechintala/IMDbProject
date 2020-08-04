from django.db import models

class UserModel(models.Model):
    id = models.AutoField(primary_key=True)
    movie_id = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    poster = models.ImageField(upload_to="movie_images/", max_length=1500)
    year = models.IntegerField()
    length = models.CharField(max_length=100)
    rating = models.CharField(max_length=50)
    rating_votes = models.CharField(max_length=50)
    plot = models.CharField(max_length=500)
    trailer_id = models.CharField(max_length=50)
    video_link = models.FileField(upload_to="movie_video/", null=True, verbose_name="")

