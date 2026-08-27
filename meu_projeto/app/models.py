from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Usuario(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='Nome')
    last_name = models.CharField(max_length=30, verbose_name='Sobrenome')
    login = models.CharField(max_length=50, unique=True, default='usuario', verbose_name='Login')
    email = models.EmailField(max_length=254, unique=True, verbose_name='E-mail')
    password = models.CharField(max_length=128, verbose_name='Senha')
    phone = models.CharField(max_length=15, blank=True, verbose_name='Telefone')
    age = models.IntegerField(
        default=18,
        validators=[MinValueValidator(1), MaxValueValidator(120)],
        verbose_name='Idade'
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
