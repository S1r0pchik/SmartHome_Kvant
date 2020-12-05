from .models import on_off_position, Termometr, Led
from django.forms import ModelForm


class PositionLedForm(ModelForm):
    class Meta:
        model = on_off_position
        fields = ["position"]


class TempForm(ModelForm):
    class Meta:
        model = Termometr
        fields = ["time", "temp"]


class LedForm(ModelForm):
    class Meta:
        model = Led
        fields = ["pos", "number", "name"]