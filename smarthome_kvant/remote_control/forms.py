from .models import Termometr, Led, LedName, PosTerm, Profile
from django.forms import ModelForm, TextInput


class TempForm(ModelForm):
    class Meta:
        model = Termometr
        fields = ["time", "temp"]


class LedForm(ModelForm):
    class Meta:
        model = Led
        fields = ["pos", "number", "name"]


class LedNameForm(ModelForm):
    class Meta:
        model = LedName
        fields = ["add_name"]
        widgets = {
            'add_name': TextInput(attrs={
                'placeholder': 'Название',
                'class': 'input',
            }),
        }


class PosTermForm(ModelForm):
    class Meta:
        model = PosTerm
        fields = ["pos_term"]

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = (
            'external_id',
            'name',
        )
        widgets = {
            'name': TextInput
        }