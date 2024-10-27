# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('text/', views.text_response, name='text_response'),
    path('html/', views.html_response, name='html_response'),
]
