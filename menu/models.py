from django.db import models


# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'category'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='menu_images', blank=True, null=True)
    price = models.PositiveIntegerField(default=0, verbose_name='Цена')
    # = models.PositiveIntegerField(default=0, verbose_name='Скидка')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE)

    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('id',)

    def __str__(self):
        return f'{self.name}'

    def display_id(self):
        return f"{self.id:03}"

    def show_price(self):
        return f'{self.price}'


