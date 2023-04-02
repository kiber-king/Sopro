from django.shortcuts import render, get_object_or_404
from . models import Task1, Task2, Task3


def index(request):
    template = 'task/index.html'
    return render(request, template)


def first_answer(request):
    template = 'task/first_answer.html'
    task = get_object_or_404(Task1)
    context = {
        'task1': task,
    }
    return render(request, template, context)


def second_answer(request):
    template = 'task/second_answer.html'
    task = get_object_or_404(Task2)
    context = {
        'task2': task,
    }
    return render(request, template, context)


def third_answer(request):
    template = 'task/third_answer.html'
    task = get_object_or_404(Task3)
    context = {
        'task3': task,
    }
    return render(request, template, context)


