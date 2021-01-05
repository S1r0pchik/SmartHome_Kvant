from django.contrib import admin

from .models import Termometr, Led, PosTerm, Rgb, Profile, Message
from .forms import ProfileForm

admin.site.register(Termometr)
admin.site.register(Led)
admin.site.register(PosTerm)
admin.site.register(Rgb)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'external_id',
                    'name'
                    )
    form = ProfileForm
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'profile',
                    'text',
                    'created_at'
                    )