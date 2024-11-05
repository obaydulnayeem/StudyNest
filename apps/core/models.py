from django.db import models
from apps.university.models import *
from django.contrib.auth.models import User



class WelcomeModel(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.university.name
    
    
