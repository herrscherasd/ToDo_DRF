from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class ToDo(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name='Название', unique=True
    )
    
    description = models.TextField(
        verbose_name='Описание')
    
    is_completed = models.BooleanField(
        default=False,
        verbose_name='Статус')
    
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания')
    
    image = models.ImageField(
        upload_to='task_images/',
        blank=True, null=True)
    
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='user_tasks',
        verbose_name='Пользователь'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = "Задачи"