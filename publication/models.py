from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse


class Series(models.Model):
    name = models.CharField(max_length=100,verbose_name='Название')
    description = models.TextField(blank=True, verbose_name="Описание")
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Серия'
        verbose_name_plural = 'Серии'

    def get_absolute_url(self):
        return reverse('seria_detail',args=[str(self.id)])


class PublicationFiles(models.Model):
    topic = models.CharField(blank=True, max_length=200, verbose_name="Тема")
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, verbose_name='Автор')
    soauthor = models.TextField(null=True, blank=True, verbose_name="Соавторы")
    comments = models.TextField(null=True, blank=True, verbose_name="Комментарии")
    file = models.FileField(upload_to='all_files', verbose_name="Файл")
    description = models.TextField(max_length=500, null=True, blank=True, verbose_name='Описание')
    date = models.DateTimeField(auto_now_add=True)
    series = models.ForeignKey(Series,on_delete=models.CASCADE,related_name='sFiles', verbose_name='Серия')
    redactor = models.BooleanField(default=False,verbose_name='Редактор')
    public = models.BooleanField(default=False,verbose_name='Опубликовать')
    archive = models.BooleanField(default=False, verbose_name='Архив')

    def __str__(self):
        return self.author.username+self.topic

    def get_absolute_url(self):
        return reverse('only_publication', args=[str(self.id)])

    class Meta:
        verbose_name = 'Файл'
        verbose_name_plural = 'Файлы'

class VestnikFiles(models.Model):
    name = models.CharField(max_length=100,verbose_name="Название вестника")
    year_variants = (
        ('2013', 2013),
        ('2014', 2014),
        ('2015', 2015),
        ('2016', 2016),
        ('2017', 2017),
        ('2018', 2018),
        ('2019', 2019),
        ('2020', 2020),
    )
    series = models.ForeignKey(Series,on_delete=models.CASCADE, verbose_name='Серия')
    year = models.CharField(max_length=4,choices=year_variants,verbose_name="Год вестника")
    file = models.FileField(upload_to='vestniks', verbose_name="Файл")

    def __str__(self):
        return self.name

    def get_name(self):
        return 'Philology vestnik '+str(self.series)+' '+self.year

    class Meta:
        verbose_name = "Вестник"
        verbose_name_plural = "Вестники"

class Pages(models.Model):
    title = models.CharField(max_length=30,verbose_name="Заголовок")
    content = models.TextField(verbose_name="Контент")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Страница"
        verbose_name_plural = "Страницы"