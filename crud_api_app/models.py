from django.db import models

# Create your models here.
class UserModel(models.Model):
    name = models.CharField(max_length=20, primary_key=True)
    email = models.EmailField()