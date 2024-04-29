from django.db import models

# Prospect model
class Prospect(models.Model):
    # foreign key of the main user table
    # user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, verbose_name=_("Usuario"))

    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    mother_last_name = models.CharField(max_length=50, default='')
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    education_level = models.CharField(max_length=100)
    currently_employed = models.BooleanField(default=False)
    sales_experience = models.BooleanField(default=False)
