# Generated by Django 3.0.5 on 2020-07-10 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0006_auto_20200709_1556'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Заголовок')),
                ('title_ru', models.CharField(max_length=30, null=True, verbose_name='Заголовок')),
                ('title_en', models.CharField(max_length=30, null=True, verbose_name='Заголовок')),
                ('title_kk', models.CharField(max_length=30, null=True, verbose_name='Заголовок')),
                ('content', models.TextField(verbose_name='Контент')),
                ('content_ru', models.TextField(null=True, verbose_name='Контент')),
                ('content_en', models.TextField(null=True, verbose_name='Контент')),
                ('content_kk', models.TextField(null=True, verbose_name='Контент')),
            ],
            options={
                'verbose_name': 'Страница',
                'verbose_name_plural': 'Страницы',
            },
        ),
    ]
