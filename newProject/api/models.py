from django.db import models

# Create your models here.
class User(models.Model):
  age = models.IntegerField()
  name = models.CharField(max_length = 100)


  def __str__(self):
    output = "User Name is " + self.name + " and age is " + str(self.age) + "."
    return output
  
