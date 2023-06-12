from django.db import models

# Create your models here.
class Shroom(models.Model):
    sci_name = models.CharField(max_length=100)
    common_name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    edible = models.BooleanField()

    def __str__(self):
        return self.common_name