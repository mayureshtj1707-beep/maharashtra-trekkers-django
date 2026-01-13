from django.db import models
from django.utils import timezone

# Create your models here.

class Trek(models.Model):
    district = models.CharField(max_length=50)  
    title = models.CharField(max_length=200)
    height = models.IntegerField()
    difficulty = models.CharField(max_length=100) 
    description = models.TextField()
    image = models.ImageField(upload_to='treks/')
    location = models.CharField(max_length=100)
    


class Booking(models.Model):
    trek = models.ForeignKey(Trek, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    mobile = models.CharField(max_length=15)
    people = models.IntegerField()
    date = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return f"{self.name} - {self.trek.title}"
