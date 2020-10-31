from django.shortcuts import render
from .forms import PositionLedForm
from .models import on_off_position


def index(request):
	return render(request, 'index.html')


def led_1(request):
	mod = 0
	form = on_off_position.objects.last()
	if str(form) == '1':
		mod = 0
	if str(form) == '0':
		mod = 1
	b = on_off_position(position=mod)
	b.save()
	return render(request, 'Led_1.html')