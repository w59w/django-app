

from django.contrib import admin
from django.urls import path, include
from myproject.myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myproject.myapp.urls')),
    path('', views.index),
]
