from django.urls import path
from . import views

urlpatterns = [
       path('',views.home, name = "home"),
       path('contact',views.contact, name = "contact"),
       path('product',views.product, name = "product"),
       path('product_details',views.product_details, name = "product_details"),
       path('cart',views.cart, name = "cart"),
       path('login',views.login, name = "login"),
       path('register',views.register, name = "register"),
       path('elements',views.elements, name = "elements"),
       path('success',views.success, name = "success"),
]
