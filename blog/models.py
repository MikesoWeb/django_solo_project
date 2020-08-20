# added

from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Название')
    body = models.TextField(db_index=True, verbose_name='Тело поста')
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')
    published = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'

    def __str__(self):
        return self.title
