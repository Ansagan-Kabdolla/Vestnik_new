from django.urls import path
from .views import *



urlpatterns = [
    path('',index, name='about'),
    path('redactor/',redactor, name='redactor'),
    path('etics/',etics, name='etics'),
    path('rules/',rules, name='rules'),
    path('archive/',archive, name='archive'),
    path('contacts/',contacts, name='contacts'),

    path('publications/',publications, name='publications'),
    path('vestniks/',vestniks,name='vestniks'),
    path('publications/<int:pk>/',only_publication, name='only_publication'),
    path('add_file/',add_file, name='add_file'),
    path('add_vestnik/',add_vestnik, name='add_vestnik'),
    path('seria_detail/<int:pk>',seria_detail, name='seria_detail'),
    path('search',search,name='search'),
    path('cabinet',cabinet,name='cabinet'),
    path('filter/',filter_publications,name='filter'),
    path('filter_ajax/',filter_ajax,name='filter_ajax'),
    path('update/<int:pk>',update,name='update'),
    path('api/',api_file,name='api_file'),
]

