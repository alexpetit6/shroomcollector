from django.db import models
from django.urls import reverse

# Create your models here.
class Shroom(models.Model):
    sci_name = models.CharField(max_length=100)
    common_name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    edible = models.BooleanField()

    def __str__(self):
        return self.common_name
    
    def get_absolute_url(self):
        return reverse('show', kwargs={'shroom_id': self.id})