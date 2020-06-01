from django.db import models

# Create your models here.
class Destination(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    username =  models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    password1 = models.CharField(max_length = 50)
    password2 = models.CharField(max_length = 50)
