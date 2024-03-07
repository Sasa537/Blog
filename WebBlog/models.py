from django.db import models

class Articles (models.Model):
    title = models.CharField('Название', max_length=50)
    preview = models.CharField('Предпросмотр', max_length=250)
    full_text = models.TextField('Вся статья')
    date = models.DateField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статьи'
        verbose_name_plural = 'Статьи'