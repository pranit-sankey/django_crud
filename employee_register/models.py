
from django.db import models

# DB models are here.

class Position(models.Model):
    title = models.CharField(max_length=50)

    #for returning title string instead of object in select position.
    def __str__(self):
        return self.title

class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3,default='dk')
    mobile= models.CharField(max_length=10)
    position= models.ForeignKey(Position,on_delete=models.CASCADE)
