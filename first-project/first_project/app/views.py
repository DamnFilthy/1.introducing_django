from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime
import os


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir'),
        'Тестовая страница': reverse('test')
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    this_moment = datetime.datetime.now()
    time_now = this_moment.time().replace(microsecond=0)
    current_time = time_now
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    folders = os.listdir(path='.')
    result = []
    for folder in folders:
        result.append('-' + folder + ' ')
    return HttpResponse(result)


def test(request):
    return HttpResponse('Это тестовая страница')
