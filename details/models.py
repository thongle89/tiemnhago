from django.db import models

# Create your models here.
class SanPham(models.Model):
	sku = models
	title = models.CharField(max_length=100)
	price = models.IntegerField()
	stock = models.BooleanField(max_length=25)
	image = models.FileField(upload_to='uploads/%Y/%m/%d/')
	brief = models.CharField(max_length=100)
	description = models.CharField(max_length=1000)