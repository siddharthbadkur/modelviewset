from django.db import models

class StudentModel(models.Model):
    name=models.CharField(max_length=45)
    city=models.CharField(max_length=42)
    roll=models.IntegerField()

    def __str__ (self):
        return self.name 
    
    

