from django import forms

from .models import Task1, Task2, Task3, Comment1, Comment2, Comment3


class Task1Form(forms.ModelForm):
    class Meta:
        model = Task1
        fields = ('answer', 'image')


class Task2Form(forms.ModelForm):
    class Meta:
        model = Task2
        fields = ('answer', 'image')


class Task3Form(forms.ModelForm):
    class Meta:
        model = Task3
        fields = ('answer', 'image')


class Comment1Form(forms.ModelForm):
    class Meta:
        model = Comment1
        fields = ('integer',)


class Comment2Form(forms.ModelForm):
    class Meta:
        model = Comment2
        fields = ('integer',)


class Comment3Form(forms.ModelForm):
    class Meta:
        model = Comment3
        fields = ('integer',)



