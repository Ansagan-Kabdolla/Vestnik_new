from django import forms
from .models import PublicationFiles,VestnikFiles

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PublicationForm(forms.ModelForm):
    class Meta:
        model = PublicationFiles
        fields = ('topic','soauthor','file','description','series')


class VestnikForm(forms.ModelForm):
    class Meta:
        model = VestnikFiles
        fields = ('name', 'file', 'series', 'year')


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, label='Логин')
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class UpdateForm(forms.ModelForm):
    class Meta:
        model = PublicationFiles
        fields = ('redactor', )