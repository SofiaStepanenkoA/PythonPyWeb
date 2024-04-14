# Generated by Django 4.2.5 on 2024-04-07 13:01

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Почта')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название')),
                ('tagline', models.TextField(verbose_name='Слоган')),
            ],
            options={
                'verbose_name': 'Блог',
                'verbose_name_plural': 'Блоги',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Название')),
                ('slug_name', models.SlugField(unique=True, verbose_name='Slug название')),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=255)),
                ('body_text', models.TextField()),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now)),
                ('mod_date', models.DateField(auto_now=True)),
                ('number_of_comments', models.IntegerField(default=0)),
                ('number_of_pingbacks', models.IntegerField(default=0)),
                ('rating', models.FloatField(default=0.0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='db_train_alternative.author')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='db_train_alternative.blog')),
                ('tags', models.ManyToManyField(related_name='entries', to='db_train_alternative.tag')),
            ],
        ),
        migrations.CreateModel(
            name='AuthorProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, help_text='Короткая биография', null=True)),
                ('phone_number', models.CharField(blank=True, help_text='Формат +79123456789', max_length=12, null=True, unique=True, validators=[django.core.validators.RegexValidator(message="Телефонный номер должен быть следующего формата: '+79123456789'.", regex='^\\+79\\d{9}$')])),
                ('city', models.CharField(blank=True, help_text='Город проживания', max_length=120, null=True)),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='db_train_alternative.author')),
            ],
        ),
    ]
