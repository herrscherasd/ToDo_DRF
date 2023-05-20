# Generated by Django 4.2.1 on 2023-05-20 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=40, unique=True, verbose_name='Имя пользователя')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Электронная почта')),
                ('phone_number', models.CharField(max_length=16, unique=True, verbose_name='Номер телефона')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('age', models.PositiveIntegerField(verbose_name='Возраст')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]