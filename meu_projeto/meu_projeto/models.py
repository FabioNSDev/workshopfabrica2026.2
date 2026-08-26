from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
class  Usuario (models.Model):
    first_name = models.CharField(max_lenght=30)
    last_name = models.CharField(max_lenght=30)
    email = models.EmailField(max_lenght=254, unique=True)
    age = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator])
    password = models.CharField(max=max_length=128)
    phone =