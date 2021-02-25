from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=250, db_index=True, verbose_name='Имя')
    slug = models.CharField(max_length=250, db_index=True, verbose_name='Ссылка', null=True, blank=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Products(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, verbose_name='Категория')
    name = models.CharField(max_length=250, db_index=True, verbose_name='Название')
    viscosity = models.CharField(
        max_length=250,
        db_index=True,
        verbose_name='Вязкость при 100°С (Нормативное значение)'
    )
    viscosity_actually = models.CharField(
        max_length=250,
        db_index=True,
        verbose_name='Вязкость при 100°С (Фактическое значение)'
    )
    index_viscosity = models.PositiveIntegerField(verbose_name='Индекс вязкости (Нормативное значение)')
    index_viscosity_actually = models.PositiveIntegerField(verbose_name='Индекс вязкости (Фактическое значение)')
    temp_flash = models.FloatField(verbose_name='Температура вспышки (Нормативное значение)')
    temp_flash_actually = models.FloatField(verbose_name='Температура вспышки (Фактическое значение)')
    temp_solidification = models.FloatField(verbose_name='Температура застывания (Нормативное значение)')
    temp_solidification_actually = models.FloatField(
        verbose_name='Температура застывания (Фактическое значение)'
    )
    base_number = models.FloatField(verbose_name='Щелочное число (Нормативное значение)', null=True, blank=True)
    base_number_actually = models.FloatField(
        verbose_name='Щелочное число (Фактическое значение)',
        null=True,
        blank=True
    )
    density = models.FloatField(verbose_name=' Плотность, при 20° С (Нормативное значение)', null=True, blank=True)
    density_actually = models.FloatField(
        verbose_name=' Плотность, при 20° С (Фактическое значение)',
        null=True,
        blank=True
    )
    color = models.FloatField(verbose_name='Цвет с разбавлением (Нормативное значение)', null=True, blank=True)
    color_actually = models.FloatField(verbose_name='Цвет с разбавлением (Фактическое значение)', null=True, blank=True)
    description = models.TextField(max_length=750, db_index=True, verbose_name='Описаие')
    image = models.ImageField(upload_to='images', verbose_name='Изображение')
    slug = models.CharField(max_length=250, db_index=True, verbose_name='Ссылка')

    class Meta:
        verbose_name = 'Масло'
        verbose_name_plural = 'Масла'

    def __str__(self):
        return self.name