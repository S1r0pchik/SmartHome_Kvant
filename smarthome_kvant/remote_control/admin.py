from django.contrib import admin
from .models import Termometr, Led

admin.site.register(Termometr),
admin.site.register(Led)