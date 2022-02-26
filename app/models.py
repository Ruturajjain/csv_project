from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    salary = models.IntegerField()
    company = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    DOJ = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    
    
    def __str__(self):
        return self.name
    
    
    
    class Meta:
        db_table = "emp"
        
        
class Company(models.Model):
    name  = models.CharField(max_length=200)