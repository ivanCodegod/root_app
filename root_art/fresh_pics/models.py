from django.db import models


class Pictures(models.Model):
    title = models.CharField('Название', max_length=150)
    description = models.TextField('Полное описание')
    date = models.DateField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новая картина'
        verbose_name_plural = 'Новые картины'
