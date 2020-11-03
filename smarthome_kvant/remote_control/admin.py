from django.contrib import admin
from .models import on_off_position, temp_on_off

admin.site.register(on_off_position)
admin.site.register(temp_on_off)