# Generated by Django 3.0.5 on 2020-06-29 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0002_auto_20200629_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicationfiles',
            name='archive',
            field=models.BooleanField(default=False, verbose_name='Архив'),
        ),
    ]