from django.shortcuts import render
from django.http import HttpResponse
from uptime import *

def index(request):
    piptime = uptime()
    data = { 'title': 'Домашняя страница', 'piptime': piptime}
    return render(request, 'remote_control/index.html', context = data)

def lamp(request):
    
    piptime = uptime()
    data = {'title': 'Управление лампочкой', 'piptime': piptime}
    return render(request, 'remote_control/lamp.html', context = data)

def temp(request):
    piptime = uptime()
    data = {'title': 'Термометр', 'piptime': piptime}
    return render(request, 'remote_control/temp.html', context = data)