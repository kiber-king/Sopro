# Generated by Django 2.2.19 on 2023-04-02 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='task/', verbose_name='Картинка')),
            ],
        ),
    ]
