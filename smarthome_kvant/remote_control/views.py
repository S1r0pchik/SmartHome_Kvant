from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import PositionLedForm
from .models import on_off_position, Termometr, rgb
from . import pyboard
import time

def index(request):
	return render(request, 'index.html')


def led_1(request):
	try:
		pyb = pyboard.Pyboard('COM7', 115200)
		pyb.enter_raw_repl()
	except:
		position = "Ошибка подключения"
		context = {
			'led_pos': position,
		}
		return render(request, 'Led_1.html', context)
	if 'dispatch' in request.POST:
		form = on_off_position.objects.last()
		if str(form) == '1':
			mod = 0
		if str(form) == '0':
			mod = 1
		bd = on_off_position(position=mod)
		bd.save()
		try:
			pyb.exec_("from pyb import Pin")
			pyb.exec_("p_out = [Pin(i, Pin.OUT_PP) for i in ('D3','D5','D6') ]")
		except:
			pass
		if mod == 0:
			try:
				pyb.exec_("p_out[0].off()")
				pyb.exec_("p_out[1].off()")
				pyb.exec_("p_out[2].off()")
				position = "Лампа сейчас выключена"
			except:
				pass
		if mod == 1:
			try:
				pyb.exec_("p_out[0].on()")
				pyb.exec_("p_out[1].on()")
				pyb.exec_("p_out[2].on()")
			except:
				pass
			position = "Лампа сейчас включена"
	else:
		form = on_off_position.objects.last()
		if form == None:
			mod = 0
			bd = on_off_position(position=mod)
			bd.save()
		if int(str(form)) == 0:
			position = "Лампа сейчас выключена"
		if int(str(form)) == 1:
			position = "Лампа сейчас включена"
	context = {
		'led_pos': position,
	}
	return render(request, 'Led_1.html', context)

def termometr(request):
	Table = Termometr.objects.order_by('-id')
	import time, random
	print(time.ctime().split()[3][3:8])
	if (len(Table) > 5):
		if (time.ctime().split()[3][3:8] == "00:00"):
			t = Termometr.objects.first()
			t.delete()
			bd = Termometr(time = time.ctime().split()[3][0:5], temp = random.randint(10, 30))
			bd.save()
	else:
		if (time.ctime().split()[3][3:8] == "00:00"):
			bd = Termometr(time = time.ctime().split()[3][0:5], temp = random.randint(10, 30))
			bd.save()
	context = {
		'Table': Table
	}
	return render(request, 'Termometr.html', context)


def rgb_lamp(request):
	color = rgb.objects.last()
	r = color.r
	g = color.g
	b = color.b
	return render(request, 'rgb_lamp.html', {"r": r, "g": g, "b": b})

def create(request):
	if request.method == "POST":
		col = rgb.objects.last()
		col.r = request.POST.get("r")
		col.g = request.POST.get("g")
		col.b = request.POST.get("b")
		col.save()
	return HttpResponseRedirect("/rgb")