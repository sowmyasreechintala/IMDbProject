from django.db import models

class AdminModel(models.Model):
    id=models.AutoField(primary_key=True)
    movie_id = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    poster = models.ImageField(upload_to="movie_images/",max_length=1500)
    year=models.CharField(null=True,blank=True,max_length=10)
    length=models.CharField(max_length=100,null=True,blank=True)
    rating=models.CharField(max_length=50,null=True)
    rating_votes=models.CharField(max_length=50,null=True,blank=True)
    plot=models.CharField(max_length=500,null=True,blank=True)
    trailer_id=models.CharField(max_length=50,blank=True)
    video_link=models.FileField(upload_to="movie_video/",null=True,verbose_name="")



