from django.shortcuts import render
from .forms import PositionLedForm
from .models import on_off_position, temp_on_off
from random import randint

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

def temp(request):
	mod = 0
	form = temp_on_off.objects.last()
	if str(form) == '1':
		mod = 0
	if str(form) == '0':
		mod = 1
	b = temp_on_off(position=mod)
	b.save()
	rand = int(randint(-30, 25))
	form = temp_on_off(temp=rand)
	form.save()
	data = {"temp": rand}
	return render(request, 'temp.html', context= data)