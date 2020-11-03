from django.shortcuts import render, redirect
from .forms import PositionLedForm
from .models import on_off_position


def index(request):
	return render(request, 'index.html')


def led_1(request):
	if 'dispatch' in request.POST:
		form = on_off_position.objects.last()
		if str(form) == '1':
			mod = 0
		if str(form) == '0':
			mod = 1
		b = on_off_position(position=mod)
		b.save()
		if mod == 0:
			position = "Лампа сейчас выключена"
		if mod == 1:
			position = "Лампа сейчас включена"
	else:
		form = on_off_position.objects.last()
		if int(str(form)) == 0:
			position = "Лампа сейчас выключена"
		if int(str(form)) == 1:
			position = "Лампа сейчас включена"
	context = {
		'led_pos': position,
	}
	return render(request, 'Led_1.html', context)