from django.db import models

# Create your models here.
class Prospect(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    education_level = models.CharField(max_length=100)
    currently_employed = models.BooleanField(default=False)
    sales_experience = models.BooleanField(default=False)
