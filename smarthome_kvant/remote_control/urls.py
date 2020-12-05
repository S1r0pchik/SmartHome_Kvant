from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('led/<int:num>', views.led_1, name="led_1"),
    path('termometr', views.termometr, name="termometr")
]

