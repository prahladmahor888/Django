from django.db import models

# Create your models here.
class UploadImage(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')

class createuser(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=200)

