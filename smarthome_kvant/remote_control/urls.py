from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('lamp/', views.lamp),
    path('temp/', views.temp),

]