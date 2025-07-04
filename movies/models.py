from django.db import models

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=200)
    genres= models.JSONField()
    rating= models.FloatField(null=True, blank=True)
    
    
    def __str__(self):
        return self.title
    
