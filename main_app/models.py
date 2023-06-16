from django.db import models
from django.urls import reverse

# Create your models here.
class Meal(models.Model):
    name = models.CharField(max_length=50)
    cuisine = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('meal_detail', kwargs={'pk': self.id})

class Shroom(models.Model):
    sci_name = models.CharField(max_length=100)
    common_name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    edible = models.BooleanField()
    meals = models.ManyToManyField(Meal)

    def __str__(self):
        return self.common_name
    
    def get_absolute_url(self):
        return reverse('show', kwargs={'shroom_id': self.id})

class Origin(models.Model):
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    date = models.DateField('Date Found')
    description = models.TextField(max_length=200)
    shroom = models.ForeignKey(Shroom, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.city}, {self.state} found on {self.date}"