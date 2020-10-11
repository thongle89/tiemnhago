from django.shortcuts import render


def home(request):
	return render(request,'index.html',{})

def contact(request):
	return render(request,'contact.html',{})

def product(request):
	return render(request,'product.html',{})

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
		
		
		
		return render(request,'index.html',{
			'user_name':user_name,
			
			})
	else:
		return render(request,'login.html',{})