from django.urls import path

from . import views

app_name = 'task'
urlpatterns = [
    path('', views.index, name='index'),
    path('task/first', views.first_answer, name='first_answer'),
    path('task/second', views.second_answer, name='second_answer'),
    path('task/third', views.third_answer, name='third_answer'),
]
