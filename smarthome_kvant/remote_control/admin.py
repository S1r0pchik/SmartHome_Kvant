from django.contrib import admin
from .models import on_off_position, Termometr, rgb

admin.site.register(on_off_position),
admin.site.register(Termometr)
admin.site.register(rgb)