from django.contrib import admin
from .models import Series,PublicationFiles,VestnikFiles,Pages
from modeltranslation.admin import TranslationAdmin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

class PagesAdminForm(forms.ModelForm):
    content = forms.CharField(label="Desc", widget=CKEditorUploadingWidget())
    content_ru = forms.CharField(label="Desc[ru]", widget=CKEditorUploadingWidget())
    content_en = forms.CharField(label="Desc[en]", widget=CKEditorUploadingWidget())
    content_kk = forms.CharField(label="Desc[kk]", widget=CKEditorUploadingWidget())
    class Meta:
        model = Pages
        fields = '__all__'

class SeriesAdminForm(forms.ModelForm):
    description = forms.CharField(label="Desc", widget = CKEditorUploadingWidget())
    description_ru = forms.CharField(label="Desc[ru]", widget = CKEditorUploadingWidget())
    description_en = forms.CharField(label="Desc[en]", widget=CKEditorUploadingWidget())
    description_kk = forms.CharField(label="Desc[kk]", widget=CKEditorUploadingWidget())
    class Meta:
        model = Series
        fields = '__all__'

@admin.register(PublicationFiles)
class PublicationFilesAdmin(admin.ModelAdmin):
    list_display = ('topic','author','soauthor','series','date','public','archive')
    list_filter = ['author','series','archive']
    search_fields = ('topic','author','soauthor')
    list_editable = ['archive','public']
    fields = (
        'topic',
        ('author','soauthor'),
        'file',
        'description',
        'date',
        'series',
        ('redactor','public'),
        'comments',
        'archive',

    )
    readonly_fields = ['topic','author','date','soauthor']

@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ('name','description')
    form = SeriesAdminForm

@admin.register(VestnikFiles)
class VestnikFilesAdmin(admin.ModelAdmin):
    list_display = ('name','series','year')
    list_filter = ['series','year']

@admin.register(Pages)
class PagesAdmin(admin.ModelAdmin):
    list_display = ('title','content')
    form = PagesAdminForm