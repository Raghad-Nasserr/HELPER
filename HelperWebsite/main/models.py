from django.db import models

# Create your models here.

#Contact form model.
class Contact(models.Model):
    name=models.CharField(max_length=700)
    email=models.EmailField()
    subject=models.CharField(max_length=700)
    message=models.TextField()