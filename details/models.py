from django.db import models

# Create your models here.
class DanhMuc(models.Model):
	category = models.CharField(max_length = 20)

	def __str__(self):
		return f"{self.category}"

class SanPham(models.Model):
	category = models.ForeignKey(DanhMuc, on_delete = models.CASCADE, related_name = "categories", default =1)
	sku = models.CharField(max_length=100,default='')
	title = models.CharField(max_length=100)
	price = models.IntegerField()
	stock = models.BooleanField(max_length=25)
	image = models.FileField(upload_to='uploads/%Y/%m/%d/',default='some_value')
	brief = models.CharField(max_length=100)
	description = models.CharField(max_length=1000)
	def __str__(self):
		return f"{self.sku} {self.image}"