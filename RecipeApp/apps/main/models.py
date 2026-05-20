from django.db import models

# Create your models here.
class Recipe(models.Model):
    
    title = models.CharField(max_length=100)
    description = models.TextField()
    ingredients = models.TextField()
    instruction = models.TextField()
    total_time = models.IntegerField()
    image = models.ImageField(upload_to='.', blank=True, null=True)
    