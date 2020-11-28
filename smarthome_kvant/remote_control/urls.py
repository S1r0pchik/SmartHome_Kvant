from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('led_1', views.led_1, name="led_1"),
    path('termometr', views.termometr, name="termometr"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('rgb', views.rgb_lamp, name="rgb"),
    path('create/', views.create)
]

