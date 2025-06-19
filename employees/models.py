from django.db import models

# Create your models here.
class Employee(models.Model):
    employee_id = models.CharField(max_length=10, unique=True)
    employee_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.employee_name} ({self.designation})"
    
    
