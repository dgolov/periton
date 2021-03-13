from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=250, db_index=True, verbose_name='Имя')
    slug = models.CharField(max_length=250, db_index=True, verbose_name='Ссылка', null=True, blank=True)
    image = models.ImageField(upload_to='categories', verbose_name='Изображение', blank=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Products(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, verbose_name='Категория')
    name = models.CharField(max_length=250, db_index=True, verbose_name='Название')
    characteristics = models.TextField(verbose_name='Характеристики', blank=True, null=True)
    description = models.TextField(max_length=750, db_index=True, verbose_name='Описаие')
    image = models.ImageField(upload_to='images', verbose_name='Изображение')
    slug = models.CharField(max_length=250, db_index=True, verbose_name='Ссылка')

    class Meta:
        verbose_name = 'Масло'
        verbose_name_plural = 'Масла'

    def __str__(self):
        return self.name