from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ('pk','slug', 'answer', 'image')
    list_editable = ('image',)
    empty_value_display = '-пусто-'


admin.site.register(Task, TaskAdmin)

