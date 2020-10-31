from .models import on_off_position
from django.forms import ModelForm


class PositionLedForm(ModelForm):
    class Meta:
        i = 1
        model = on_off_position
        fields = ["position"]