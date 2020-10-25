from django.db import models

# Create your models here.
class DanhMuc(models.Model):
	category = models.CharField(max_length = 20)
	# code = models.CharField(max_length = 3)

	def __str__(self):
		return f"{self.category}"

class SanPham(models.Model):
	category = models.ForeignKey(DanhMuc, on_delete = models.CASCADE, related_name = "categories", default =1)
	sku = models.AutoField(primary_key = True)
	title = models.CharField(max_length=100)
	price = models.IntegerField()
	stock = models.BooleanField(max_length=25)
	image = models.ImageField(upload_to='%Y/%m/%d/')
	brief = models.TextField(max_length=150)
	description = models.TextField(max_length=1000)
	def __str__(self):
		return f"{self.sku} {self.image}"