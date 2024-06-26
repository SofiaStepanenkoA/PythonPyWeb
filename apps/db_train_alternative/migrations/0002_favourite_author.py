# Generated by Django 4.2.5 on 2024-04-14 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db_train_alternative', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='favourite_author',
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
    ]
