from django.db import models

# Create your models here.
class Student(models.Model):
   roll = models.CharField(max_length=50,unique=True)
   name = models.CharField(max_length=100)
   dob = models.DateField()

   def __str__(self):
       return self.roll

class Marks(models.Model):
   roll = models.ForeignKey(Student,on_delete=models.CASCADE)
   mark = models.IntegerField()


   def __str__(self):
       return self.roll