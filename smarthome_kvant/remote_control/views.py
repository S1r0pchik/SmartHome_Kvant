from django.shortcuts import render
from .forms import PositionLedForm
from .models import on_off_position, Termometr, Led
from . import pyboard
import time

def index(request, num = 1):
	form = Led.objects.all()
	context = {
		"num": num,
		"Names": form,
	}
	return render(request, 'index.html', context)


def led_1(request, num = str(Led.objects.last()).split()[1]):
	# try:
	# 	pyb = pyboard.Pyboard('COM7', 115200)
	# 	pyb.enter_raw_repl()
	# except:
	# 	position = "Ошибка подключения"
	# 	context = {
	# 		'led_pos': position,
	# 	}
	# 	return render(request, 'Led_1.html', context)
	form = Led.objects.get(number = num)
	if str(form.pos) == '1':
		mod = 1
	if str(form.pos) == '0':
		mod = 0
	if 'dispatch' in request.POST:
		Led.objects.get(number = num)
		if str(form.pos) == '1':
			mod = 0
		if str(form.pos) == '0':
			mod = 1
		bd = Led.objects.get(number = num)
		bd.pos = mod
		bd.save()
	# 	try:
	# 		pyb.exec_("from pyb import Pin")
	# 		pyb.exec_("p_out = [Pin(i, Pin.OUT_PP) for i in ('D3','D5','D6') ]")
	# 	except:
	# 		pass
	# 	if mod == 0:
	# 		try:
	# 			pyb.exec_("p_out[0].off()")
	# 			pyb.exec_("p_out[1].off()")
	# 			pyb.exec_("p_out[2].off()")
	# 			position = "Лампа сейчас выключена"
	# 		except:
	# 			pass
	# 	if mod == 1:
	# 		try:
	# 			pyb.exec_("p_out[0].on()")
	# 			pyb.exec_("p_out[1].on()")
	# 			pyb.exec_("p_out[2].on()")
	# 		except:
	# 			pass
	# 		position = "Лампа сейчас включена"
	if (mod == 0):
		position = "Лампа сейчас выключена"
	if (mod == 1):
		position = "Лампа сейчас включена"
	context = {
		"pos": position,
		"name": Led.objects.get(number = num).name
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