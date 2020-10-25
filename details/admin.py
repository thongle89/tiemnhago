from django.contrib import admin
from .models import *
# Register your models here.
class SanPhamAdmin(admin.ModelAdmin):
    list_display = ("title","category","sku", "price", "stock")


admin.site.register(SanPham,SanPhamAdmin)
admin.site.register(DanhMuc)
