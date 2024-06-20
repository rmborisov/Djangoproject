from django.db import models

# Create your models here.

class MusicTask(models.Model):
    title = models.CharField('Название', max_length=100)
    musictask = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
