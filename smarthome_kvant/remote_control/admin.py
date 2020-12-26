from django.contrib import admin
from .models import Termometr, Led, PosTerm, Rgb

admin.site.register(Termometr),
admin.site.register(Led),
admin.site.register(PosTerm)
admin.site.register(Rgb)