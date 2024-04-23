from django.db import models

# Create your models here.
class Prospect(models.Model):
    EDUCATION_LEVEL_CHOICES = [
        ('High School', 'Secundaria'),
        ('Preparatory', 'Preparatoria'),
        ('Bachelor', 'Licenciatura')
    ]

    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    education_level = models.CharField(max_length=50, choices=EDUCATION_LEVEL_CHOICES)
    currently_employed = models.BooleanField(default=False)
    sales_experience = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name
