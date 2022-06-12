from pyexpat import model
from django.db import models

# Create your models here.
class Student(models.Model):
    sid = models.IntegerField()
    roll_no = models.IntegerField()
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    
    
    
