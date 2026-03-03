from django.db import models
from django.urls import reverse 
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model): 
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=250, blank=True, default='')

    def __str__(self):
        return self.name 
    
    def get_absolute_url(self):
        return reverse('category-detail', kwargs={'pk': self.pk})

    
CARE_TYPE = (
    ("W", "Water"), 
    ("F", "Food"), 
    ("T", "Talk")
    )

TIMES = (
    ('AM', 'Morning'), 
    ('PM', 'Afternoon'), 
    ('N', 'Night'), 
)

SIZES = (
    ("S", "Small"), 
    ("M", "Medium"), 
    ("L", "Large")
    )

class Plant(models.Model): 
    name = models.CharField(max_length=100)
    size = models.CharField(
        max_length=1, 
        choices = SIZES,
        default = SIZES[0][0], 
    )
    notes = models.TextField(blank=True, default='')
    categories = models.ManyToManyField(Category)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    image_url = models.URLField(
        'Plant Image URL', 
        max_length = 500, 
        blank = True, 
        null = True 
    )

    def __str__(self):
        return self.name 
    
    def get_absolute_url(self):
        return reverse('plant-detail', kwargs={'pk': self.id})

class Care(models.Model): 
    date = models.DateField("CARE DATE")
    care_type = models.CharField(
        max_length = 1,  
        choices = CARE_TYPE, 
        default = CARE_TYPE[0][0]
    )
    time_of_day = models.CharField(
        max_length = 2, 
        choices = TIMES, 
        blank = True, 
        null = True 
    )
    plant = models.ForeignKey(Plant, on_delete = models.CASCADE)

    def __str__(self):
        time_str = f"{self.get_time_of_day_display()})" if self.time_of_day else ""
        return f"{self.get_care_type_display()}{time_str} on {self.date}"
    
    class Meta: 
        ordering = ["-date"]
    
