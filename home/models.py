from django.db import models

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Student(models.Model):
    name = models.CharField(max_length=30) 
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    age = models.IntegerField() 
    
    def __str__(self):
        return f"{self.name} - {self.course}"
