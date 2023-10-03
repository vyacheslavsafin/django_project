from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Post(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    slug = models.CharField(max_length=150, verbose_name='slug')
    content = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to='blog/', **NULLABLE, verbose_name='Превью')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    publication_sign = models.BooleanField(default=True, verbose_name='Публикация')
    views_count = models.IntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи '