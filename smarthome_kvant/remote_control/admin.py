from django.contrib import admin
from .models import Termometr, Led, PosTerm

admin.site.register(Termometr),
admin.site.register(Led),
admin.site.register(PosTerm)