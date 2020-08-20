# added

from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Название статьи')
    body = models.TextField(blank=True, db_index=True, verbose_name='Тело статьи')
    image = models.ImageField(verbose_name='Изображение', null=True, upload_to='static/media', blank=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    published = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'
        ordering = ['-published']

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=20, db_index=True, verbose_name='Имя тега')

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'
        ordering = ['title']

    def __str__(self):
        return self.title
