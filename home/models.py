from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=50)
    date = models.DateField()
    message =models.TextField()
    def __str__(self):
        return self.name
    
