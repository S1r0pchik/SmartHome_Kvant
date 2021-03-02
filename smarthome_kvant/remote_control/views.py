from django.shortcuts import render
from .forms import LedNameForm
from django.contrib.auth.models import User
from .models import Termometr, Led, LedName, PosTerm
from . import pyboard, LED
import time

def index(request, num = 1):
	form = Led.objects.all()
	InputForm = LedNameForm()
	if 'Add' in request.POST:
		temp_form = LedNameForm(request.POST)
		if temp_form.is_valid():
			name = temp_form.cleaned_data['add_name']
			try:
				prev = int(Led.objects.last().number)
			except:
				prev = 0
			database = Led(pos=0, number=prev + 1, name=name)
			database.save()
	context = {
		"num": num,
		"Names": form,
		"Form": InputForm
	}
	return render(request, 'index_dark.html', context)


try:
	number = str(Led.objects.last()).split()[1]
except:
	number = 1


def led_1(request, num=number):
	try:
		pyb = pyboard.Pyboard('COM20', 115200)
		pyb.enter_raw_repl()
		print("successful connection")
	except:
		position = "Ошибка подключения"
		context = {
			'led_pos': position,
		}
		return render(request, 'Led_dark.html', context)

	form = Led.objects.get(number=num)
	if str(form.pos) == '1':
		mod = 1
	if str(form.pos) == '0':
		mod = 0

	if 'dispatch' in request.POST:
		Led.objects.get(number=num)
		if str(form.pos) == '1':
			mod = 0
		if str(form.pos) == '0':
			mod = 1
		bd = Led.objects.get(number=num)
		bd.pos = mod
		bd.save()

		try:
			pyb.exec_("from pyb import Pin")
			pyb.exec_("LEDS = [Pin(i, Pin.OUT_PP) for i in ('D3','D5','D6') ]")
		except:
			pass
		if mod == 0:
			try:
				pyb.exec_("LEDS[{0}].off()".format(int(form.number) - 1))
				position = "Лампа сейчас выключена"
			except:
				pass
		if mod == 1:
			try:
				pyb.exec_("LEDS[{0}].on()".format(int(form.number) - 1))
			except:
				pass
			position = "Лампа сейчас включена"

	if mod == 0:
		position = "Лампа сейчас выключена"
	if mod == 1:
		position = "Лампа сейчас включена"
	context = {
		"pos": position,
		"name": Led.objects.get(number=num).name
	}
	return render(request, 'Led_dark.html', context)

def termometr(request):
	Table = Termometr.objects.order_by('-id')
	pos = PosTerm.objects.first()
	import time, random

	if pos == None:
		data = PosTerm(pos_term='0')
		data.save()

	if 'change_pos' in request.POST:
		if str(pos) == '0':
			pos.pos_term = '1'
		else:
			pos.pos_term = '0'
		pos.save()
	if str(pos) == '1':
		if 'Temp' in request.POST:
			if (len(Table) >= 5):
				t = Termometr.objects.first()
				t.delete()
				bd = Termometr(time = time.ctime().split()[3][0:5], temp = random.randint(10, 30))
				bd.save()
			else:
				bd = Termometr(time = time.ctime().split()[3][0:5], temp = random.randint(10, 30))
				bd.save()
		else:
			if (len(Table) > 5):
				if (time.ctime().split()[3][3:8] == "00:00"):
					t = Termometr.objects.first()
					t.delete()
					bd = Termometr(time=time.ctime().split()[3][0:5], temp=random.randint(10, 30))
					bd.save()
			else:
				if (time.ctime().split()[3][3:8] == "00:00"):
					bd = Termometr(time=time.ctime().split()[3][0:5], temp=random.randint(10, 30))
					bd.save()
	Table = Termometr.objects.order_by('-id')
	context = {
		'Table': Table
	}
	return render(request, 'Termometr_dark.html', context)