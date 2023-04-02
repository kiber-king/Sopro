from django.contrib import admin

from .models import Task1, Task2, Task3, Comment1, Comment3, Comment2


class Task1Admin(admin.ModelAdmin):
    list_display = ('pk', 'answer', 'image')
    list_editable = ('image',)
    empty_value_display = '-пусто-'


admin.site.register(Task1, Task1Admin)


class Task2Admin(admin.ModelAdmin):
    list_display = ('pk', 'answer', 'image')
    list_editable = ('image',)
    empty_value_display = '-пусто-'


admin.site.register(Task2, Task2Admin)


class Task3Admin(admin.ModelAdmin):
    list_display = ('pk', 'answer', 'image')
    list_editable = ('image',)
    empty_value_display = '-пусто-'


admin.site.register(Task3, Task3Admin)
