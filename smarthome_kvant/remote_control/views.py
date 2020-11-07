from django.shortcuts import render, redirect
from .forms import PositionLedForm
from .models import on_off_position, temp_on_off
from random import randint

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

def temp(request):
	mod = 0
	form = temp_on_off.objects.last()
	if str(form) == '1':
		mod = 0
	if str(form) == '0':
		mod = 1
	rand = int(randint(-30, 25))
	b = temp_on_off(position=mod, temp=rand)
	b.save()
	form = temp_on_off.objects.last()
	if form == None:
		mod = 0
		bd = temp_on_off(position=mod, temp=rand)
		bd.save()
	data = {
		"temp": rand
	}
	return render(request, 'temp.html', context= data)