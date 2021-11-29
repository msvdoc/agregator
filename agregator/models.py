from django.db import models

# Create your models here.
class ShoesData(models.Model):
	name = models.CharField(max_length=150, db_index=True, verbose_name="Название")
	magazineName = models.CharField(max_length=200, verbose_name="Магазин")
	description = models.TextField(verbose_name="Описание", null=True, blank=True)
	sezon = models.CharField(max_length=50, verbose_name="Сезон", null=True, blank=True)
	def __str__(self):
		return self.name
	class Meta:
		verbose_name = "Обувь"
		verbose_name_plural = "Обувь"
		ordering = ['name']

class ShoesPrice(models.Model):
	timeScan = models.DateTimeField(auto_now_add=True, verbose_name="Время сканирования")
	priceShoes = models.PositiveIntegerField(verbose_name="Цена")
	name = models.ForeignKey('ShoesData', on_delete=models.CASCADE, verbose_name='Название')
	class Meta:
		verbose_name = "Текущая цена"
		verbose_name_plural = "Текущие цены"