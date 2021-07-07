from django.db import models


class Pictures(models.Model):
    title = models.CharField('Название', max_length=150)
    description = models.TextField('Полное описание')
    image = models.ImageField('Фото', upload_to='photo_categories', blank=True)
    date = models.DateField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новая картина'
        verbose_name_plural = 'Новые картины'
