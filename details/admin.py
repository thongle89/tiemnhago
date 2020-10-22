from django.contrib import admin
from .models import *
# Register your models here.
class SanPhamAdmin(admin.ModelAdmin):
    list_display = ("id", "sku", "price", "stock")


admin.site.register(SanPham,SanPhamAdmin)
admin.site.register(DanhMuc)
