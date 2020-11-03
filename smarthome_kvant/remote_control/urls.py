from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('led_1', views.led_1, name="led_1")
]

