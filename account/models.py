from django.db import models

# Create your models here.
class FormModel(models.Model):
    username = models.CharField(max_length=10)
    surname = models.CharField(max_length=10)
    age = models.CharField(max_length=10)
    job = models.CharField(max_length=10)
    university = models.CharField(max_length=10)
    experience = models.TextField(max_length=300)
    hobies = models.TextField(max_length=100)
    languages = models.TextField(max_length=100)

    def __str__(self):
        return self.username
    
class ContactModel(models.Model):
    username = models.CharField(max_length=10)
    surname = models.CharField(max_length=10)
    message = models.TextField(max_length=200)

    def __str__(self):
        return self.username