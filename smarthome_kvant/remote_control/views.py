from django.shortcuts import render
from .forms import LedNameForm
from .models import Termometr, Led, LedName, PosTerm
from .moduls import *
from . import pyboard
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
			database = Led(pos = 0, number = prev + 1, name = name)
			database.save()
	context = {
		"num": num,
		"Names": form,
		"Form": InputForm
	}
	return render(request, 'index.html', context)

try:
	number = str(Led.objects.last()).split()[1]
except:
	number = 1

def led_1(request, num = number):
	connected = True
	# try:
	# 	try_to_connect()
	#	connected = True
	# except:
	# 	position = "Ошибка подключения"
	# 	context = {
	# 		'led_pos': position,
	# 	}
	#	connected = False
	if (connected == True):
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
		# 		connecting()
		# 	except:
		# 		pass
		# 	if mod == 0:
		# 		off_led()
		# 		position = "Лампа сейчас выключена"
		# 	if mod == 1:
		# 		on_led()
		# 		position = "Лампа сейчас включена"
		if (mod == 0):
			position = "Лампа сейчас выключена"
		if (mod == 1):
			position = "Лампа сейчас включена"
	context = {
		"pos": position,
		"name": Led.objects.get(number = num).name,
		"img": Led.objects.get(number = num).pos
	}
	return render(request, 'Led_1.html', context)

def termometr(request):
	Table = Termometr.objects.order_by('-id')
	pos = PosTerm.objects.last()
	import time, random
	if 'change_pos' in request.POST:
		if str(pos) == '1':
			pos.pos_term = '0'
		elif str(pos) == '0':
			pos.pos_term = '1'
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
	if (str(pos) == '0'):
		Pos = "Термометр сейчас выключен"
	if (str(pos) == '1'):
		Pos = "Термометр сейчас включен"
	Table = Termometr.objects.order_by('-id')
	context = {
		'Table': Table,
		'Pos': Pos
	}
	return render(request, 'Termometr.html', context)