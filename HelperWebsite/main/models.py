from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Contact form model.
class Contact(models.Model):
    name=models.CharField(max_length=700)
    email=models.EmailField()
    subject=models.CharField(max_length=700)
    message=models.TextField()


# Help request form model.
class HelpRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    help_description=models.TextField()
    phone_number=models.IntegerField()

# Helper form model.
class Helper(models.Model):
    name=models.CharField(max_length=700)
    email=models.EmailField()
    phone_number=models.IntegerField()
    description_of_experiences=models.TextField()
    helper_cv= models.FileField(upload_to="uploads/")


