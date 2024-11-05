from django.db import models
from choices.location import *

# Create your models here.
class CollegeType(models.Model):
    type = models.CharField(max_length=100, blank = True, null = True)
    
    def __str__(self):
        return f'{self.type}'
    
class College(models.Model):
    name = models.CharField(max_length=200)
    former_name = models.CharField(max_length=200, blank = True, null = True)
    acronym = models.CharField(max_length=20, blank = True, null = True)
    college_type = models.ForeignKey(CollegeType, on_delete=models.CASCADE, blank = True, null = True)
    eiin = models.PositiveIntegerField(blank=True, null=True)
    established = models.IntegerField(blank=True, null=True)
    history = models.TextField(blank = True, null = True)
    location_division = models.CharField(max_length=100, blank = True, null = True, choices = DIVISIONS)
    location_district = models.CharField(max_length=100, blank = True, null = True, choices = DISTRICTS)
    location_permanent_campus = models.CharField(max_length=200, blank = True, null = True)
    # campus_area = models.DecimalField(max_digits=4, decimal_places=2, blank = True, null = True)
    campus_area = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    motto_bangla = models.CharField(max_length=200, blank = True, null = True)
    motto_english = models.CharField(max_length=200, blank = True, null = True)
    logo = models.ImageField(upload_to='college/college_logos/', blank = True, null = True)
    num_regular_students = models.PositiveIntegerField(blank = True, null = True)
    num_academic_staff = models.PositiveIntegerField(blank = True, null = True)
    num_residence_hall = models.PositiveIntegerField(blank = True, null = True)
    website = models.URLField(blank = True, null = True)
    contact_number = models.CharField(max_length=50, blank = True, null = True)
    colors = models.CharField(max_length=100, blank = True, null = True)
    
    def __str__(self):
        return f'{self.name}'