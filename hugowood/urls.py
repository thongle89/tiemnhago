from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('daika/', admin.site.urls),
    path('',include('website.urls')),
    path('details/',include('details.urls')),
]