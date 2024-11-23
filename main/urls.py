from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Главная страница
    path('gallery/', views.gallery, name='gallery'),  # Галерея
]
