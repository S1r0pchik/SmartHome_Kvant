from django.shortcuts import render
from .forms import LedNameForm
from .models import Termometr, Led, LedName, PosTerm, Rgb
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
		"Form": InputForm,
		"title": "Главная страницв | Smart Home"
	}
	return render(request, 'index.html', context)

try:
	number = str(Led.objects.last()).split()[1]
except:
	number = 1
def led_1(request, num = number):
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
		"name": Led.objects.get(number = num).name,
		"title": "Управление лампочками | Smart Home"
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
	Table = Termometr.objects.order_by('-id')
	context = {
		'Table': Table,
		"title": "Управление термометром | Smart Home"
	}
	return render(request, 'Termometr.html', context)

def rgb_lamp(request):
	color = Rgb.objects.last()
	r = color.r
	g = color.g
	b = color.b
	context = {
		"r": r,
		"g": g,
		"b": b,
		"title": "Управление RGB лентой | Smart Home"
	}
	return render(request, 'rgb_lamp.html', )

def create(request):
	if request.method == "POST":
		col = rgb.objects.last()
		col.r = request.POST.get("r")
		col.g = request.POST.get("g")
		col.b = request.POST.get("b")
		col.save()
	return HttpResponseRedirect("/rgb")