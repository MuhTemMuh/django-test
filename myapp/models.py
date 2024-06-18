from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=255, verbose_name='Имя')
    slug=models.SlugField(max_length=255, verbose_name='Ссылка')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.pk})

class Posts(models.Model):
    title=models.CharField(max_length=255)
    content=models.CharField(max_length=110)
    is_published=models.BooleanField(blank=True,default=True)
    photo=models.ImageField('photo=photo/%Y/%n/%d/')
    time=models.DateField()
    time_create=models.DateTimeField(auto_now_add=True)
    time_update=models.DateTimeField(auto_now_add=True)
    categoria=models.ForeignKey(Category, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})
    
    class meta:
        verbose_name="Пост"
        verbose_name_plural="Посты"
    
    def __main__(self):
        return self.time_create


