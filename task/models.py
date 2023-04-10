from django.db import models


class Task(models.Model):
    slug = models.SlugField(unique=True)
    answer = models.TextField()
    image = models.ImageField(
        'Картинка',
        upload_to='task/',
        blank=True
    )

    class Meta:
        default_related_name = 'task'
