# Generated by Django 3.0.5 on 2020-07-01 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publication', '0003_publicationfiles_archive'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicationfiles',
            name='comments',
            field=models.TextField(blank=True, null=True, verbose_name='Комментарии'),
        ),
        migrations.AddField(
            model_name='publicationfiles',
            name='soauthor',
            field=models.TextField(blank=True, null=True, verbose_name='Соавторы'),
        ),
        migrations.AddField(
            model_name='publicationfiles',
            name='topic',
            field=models.CharField(blank=True, max_length=200, verbose_name='Тема'),
        ),
        migrations.AddField(
            model_name='series',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='publicationfiles',
            name='file',
            field=models.FileField(upload_to='all_files', verbose_name='Файл'),
        ),
        migrations.CreateModel(
            name='VestnikFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название вестника')),
                ('year', models.CharField(choices=[('2013', 2013), ('2014', 2014), ('2015', 2015), ('2016', 2016), ('2017', 2017), ('2018', 2018), ('2019', 2019), ('2020', 2020)], max_length=4, verbose_name='Год вестника')),
                ('file', models.FileField(upload_to='vestniks', verbose_name='Файл')),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publication.Series', verbose_name='Серия')),
            ],
            options={
                'verbose_name': 'Вестник',
                'verbose_name_plural': 'Вестники',
            },
        ),
    ]
