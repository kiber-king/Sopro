from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from .models import Task


def get_paginator(request, obj_list):
    paginator = Paginator(obj_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj


def index(request):
    template = 'task/index.html'
    return render(request, template)


def answer(request):
    template = 'task/answer_list.html'
    tasks = Task.objects.all()
    page_obj = get_paginator(request, tasks)
    context = {
        'page_obj': page_obj
    }
    return render(request, template, context)


def task_detail(request, slug):
    task = get_object_or_404(Task, slug=slug)
    templates = {
        '2_43_2': 'task/2_43_2.html',
        '2_43_3': 'task/2_43_3.html',
        '2_43_4': 'task/2_43_4.html',
        '26_17': 'task/26_17.html',
        '26_18': 'task/26_18.html',
        '26_19': 'task/26_19.html',
        '26_20': 'task/26_20.html',
    }
    context = {
        'task': task,
    }
    return render(request, templates[slug], context)

