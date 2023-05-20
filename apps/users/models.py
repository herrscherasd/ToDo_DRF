from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username = models.CharField(
        max_length=40,
        unique=True,
        verbose_name='Имя пользователя')
    
    email = models.EmailField(
        unique=True,
        verbose_name='Электронная почта')
    
    phone_number = models.CharField(
        unique=True,
        max_length=16,
        verbose_name='Номер телефона')
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания')
    
    age = models.PositiveIntegerField(
        verbose_name='Возраст')
    
    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"