from django.db import models
from django.urls import reverse 
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model): 
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=250, blank=True, default='')

    def __str__(self):
        return self.name 
    

SIZES = (("S", "Small"), ("M", "Medium"), ("L", "Large"))

class Plant(models.Model): 
    name = models.CharField(max_length=100)
    size = models.CharField(
        max_length=1, 
        choices = SIZES,
        default = SIZES[0][0], 
    )
    notes = models.TextField(blank=True, default='')
    categories = models.ManyToManyField(Category)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name 
    
CARE_TYPE = (("W", "Water"), ("F", "Food"), ("T", "Talk"))

class Care(models.Model): 
    date = models.DateField
    care_type = models.CharField(
        max_length = 1,  
        choices = CARE_TYPE, 
        default = CARE_TYPE[0][0], 
    )
    plant = models.ForeignKey(Plant, on_delete = models.CASCADE)

    def __str__(self):
        return f"{self.get_care_display()} on {self.date}"
    
