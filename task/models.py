from django.db import models


class Task1(models.Model):
    answer = models.TextField()
    image = models.ImageField(
        'Картинка',
        upload_to='task/',
        blank=True
    )


class Task2(models.Model):
    answer = models.TextField()
    image = models.ImageField(
        'Картинка',
        upload_to='task/',
        blank=True
    )


class Task3(models.Model):
    answer = models.TextField()
    image = models.ImageField(
        'Картинка',
        upload_to='task/',
        blank=True
    )


class Comment1(models.Model):
    integer = models.IntegerField()
    task = models.ForeignKey(Task1,
                             blank=True,
                             null=True,
                             on_delete=models.CASCADE,
                             related_name='comments')


class Comment2(models.Model):
    integer = models.IntegerField()
    task = models.ForeignKey(Task2,
                             blank=True,
                             null=True,
                             on_delete=models.CASCADE,
                             related_name='comments')


class Comment3(models.Model):
    integer = models.IntegerField()
    task = models.ForeignKey(Task3,
                             blank=True,
                             null=True,
                             on_delete=models.CASCADE,
                             related_name='comments')
