from django.db import models
from djongo import models
from unittest.util import _MAX_LENGTH
# Create your models here.
class signin(models.Model):
    id = models.ObjectIdField()
    Username = models.CharField(max_length=250, blank=False,unique=True)
    Password = models.CharField(max_length=250, blank=False,unique=True)

    FaviouriteCity = models.CharField(max_length=200, blank=False,unique=True)

    def str(self):
           return self.Username
    
    class Meta:
        verbose_name_plural = "Contact"