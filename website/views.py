from django.shortcuts import render
from details.models import *

def home(request):
	if "user_name" not in request.session:
		request.session["user_name"] = []

	return render(request,'index.html',{
		"user_name" : request.session["user_name"],
		"categories": DanhMuc.objects.all(),
		})

def contact(request):
	return render(request,'contact.html',{})

def product(request):
	return render(request,'product.html',{
		"categories": DanhMuc.objects.all(),
		"products":SanPham.objects.all(),
		})

def product_details(request):
	return render(request,'product_details.html',{})

def cart(request):
	return render(request,'cart.html',{})

def login(request):
	return render(request,'login.html',{})

def register(request):
	return render(request,'register.html',{})

def elements(request):
	return render(request,'elements.html',{})

def success(request):
	if request.method == "POST":

		user_name = request.POST['user_name']
		request.session["user_name"]=user_name
		
		
		return render(request,'index.html',{
			'user_name':user_name,
			
			})
	else:
		return render(request,'login.html',{})