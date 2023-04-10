from django.urls import path

from . import views

app_name = 'task'
urlpatterns = [
    path('', views.index, name='index'),
    path('answer_list/', views.answer, name='answer_list'),
    path('task/<slug:slug>/', views.task_detail, name='task_detail'),
]
