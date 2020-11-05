from django.db import models

# Create your models here.
class DanhMuc(models.Model):
	code = models.CharField(max_length = 3)
	category = models.CharField(max_length = 20)
	

	def __str__(self):
		return f"{self.category} ({self.code})"

class SanPham(models.Model):
	category = models.ForeignKey(DanhMuc, on_delete = models.CASCADE, related_name = "categories")
	sku = models.AutoField(primary_key = True)
	title = models.CharField(max_length=100)
	price = models.IntegerField()
	stock = models.BooleanField(max_length=25)
	image = models.ImageField(upload_to='%Y/%m/%d/')
	brief = models.TextField(max_length=150)
	description = models.TextField(max_length=1000)
	def __str__(self):
		return f" {self.title} ({self.sku})"

class ThuVien(models.Model):
	title = models.ForeignKey(SanPham,on_delete = models.CASCADE,related_name= "titles")
	image = models.ImageField(upload_to='%Y/%m/%d/')
	def __str__(self):
		return f"{self.title}"
