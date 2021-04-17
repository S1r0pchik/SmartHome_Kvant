from .models import Termometr, Led, LedName, PosTerm, Users
from django.forms import ModelForm, TextInput


class TempForm(ModelForm):
    class Meta:
        model = Termometr
        fields = ["time", "temp"]


class LedForm(ModelForm):
    class Meta:
        model = Led
        fields = ["pos", "number", "name"]

class UserForm(ModelForm):
    class Meta:
        model = Users
        fields = ["user"]

class LedNameForm(ModelForm):
    class Meta:
        model = LedName
        fields = ["add_name"]
        widgets = {
            'add_name': TextInput(attrs={
                'placeholder': 'Название',
                'autocomplete': 'off',
                'class': 'input',
            }),
        }


class PosTermForm(ModelForm):
    class Meta:
        model = PosTerm
        fields = ["pos_term"]