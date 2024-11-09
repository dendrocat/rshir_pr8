from django.db import models
from django.urls import reverse_lazy



# Create your models here.
class Material(models.Model):
    name = models.CharField(max_length=40, verbose_name="Название")
    
    class Meta:
        verbose_name = "Материал"
        verbose_name_plural = "Материалы"
        ordering = ["pk"]
    
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    price = models.IntegerField(verbose_name="Цена")
    mat = models.ForeignKey(Material, on_delete=models.PROTECT, verbose_name="Материал")
    
    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["pk"]
    
    def __str__(self):
        return self.name
    
    
class PDF(models.Model):
    name = models.TextField(verbose_name="Название")
    file = models.FileField(upload_to="uploads/")
    size = models.IntegerField(verbose_name="Размер")

    class Meta:
        verbose_name = "PDF-файл"
        verbose_name_plural = "PDF-файлы"
        ordering = ['pk']
    
    def get_absolute_url(self):
        return reverse_lazy("download-pdf", kwargs={"name": self.name})
    
    
    def __str__(self):
        return self.name
    
    
class City(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    country = models.CharField(max_length=100, verbose_name="Страна")
    mayor = models.CharField(max_length=50, verbose_name="Мэр")
    postcode = models.CharField(max_length=6, verbose_name="Индекс")
    number = models.IntegerField(verbose_name="Численность населения")
    
    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"
        ordering = ['-number']
    
    
    def __str__(self):
        return self.name
    
    
class Graphics(models.Model):
    name = models.CharField(max_length=50, verbose_name="Тип графика")
    file = models.ImageField(upload_to="charts/")
    
    class Meta:
        verbose_name = "График"
        verbose_name_plural = "Графики"
        ordering = ['pk']
    
    def __str__(self):
        return self.name
    