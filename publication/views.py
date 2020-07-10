from django.shortcuts import render,redirect
from .models import Series,PublicationFiles,VestnikFiles,Pages
from .forms import PublicationForm,VestnikForm,UpdateForm
from django.http import JsonResponse
from django.http import HttpResponse

from django.contrib.auth import login, authenticate
from django.contrib.auth.models import Group
from .forms import SignUpForm

from django.db.models import Q


def index(request):
    q = Pages.objects.get(pk=1)
    title = q.title
    content = q.content
    return render(request,'about.html',{'title':title,'content':content})

def redactor(request):
    q = Pages.objects.get(pk=2)
    title = q.title
    content = q.content

    return render(request,'redaction.html',{'title':title,'content':content})

def etics(request):
    q = Pages.objects.get(pk=3)
    title = q.title
    content = q.content

    return render(request,'redaction.html',{'title':title,'content':content})

def rules(request):
    q = Pages.objects.get(pk=4)
    title = q.title
    content = q.content

    return render(request, 'redaction.html', {'title': title, 'content': content})

def archive(request):
    return render(request,'archive.html')

def contacts(request):
    q = Pages.objects.get(pk=5)
    title = q.title
    content = q.content

    return render(request, 'redaction.html', {'title': title, 'content': content})


def publications(request):
    files = PublicationFiles.objects.filter(public=True)
    return render(request,'publications.html',{'files':files})

def only_publication(request,pk):
    file = PublicationFiles.objects.get(pk=pk)
    return render(request,'only_publication.html',{'file':file})

def add_file(request):
    if request.method == "POST":
        form = PublicationForm(request.POST,request.FILES)
        if form.is_valid():
            public = form.save(commit=False)
            public.author = request.user
            public.save()
            return redirect('publications')
    else:
        form = PublicationForm()
    return render(request,'add_file.html',{'form':form})


def add_vestnik(request):
    if request.method == "POST":
        form = VestnikForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('vestniks')
    else:
        form = VestnikForm()
    return render(request, 'add_vestnik.html', {'form': form})

def vestniks(request):
    vs =  VestnikFiles.objects.all()
    return render(request,'vestniks.html',{'vs':vs})

def seria_detail(request,pk):
    seria = Series.objects.get(pk=pk)
    return render(request,'seria_detail.html',{'seria':seria})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():#Если форма заполнена правильно
            form.save()#Создаем пользователя
            username = form.cleaned_data.get('username')#с именем
            raw_password = form.cleaned_data.get('password1')# и паролем
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('about')#страница редиректа после регистрации
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def search(request):
    query = request.GET.get('q')
    files = PublicationFiles.objects.filter(
            Q(topic__icontains=query) | Q(author__username__icontains=query) | Q(soauthor__icontains=query)
        )
    return render(request, 'search_result.html', {'files': files})

def cabinet(request):
    user = request.user
    redactors = Group.objects.get(name="Redactors").user_set.all()
    if user in redactors:
        red_publications = PublicationFiles.objects.filter(redactor=False)
        return render(request,'cabinet_redactor.html',{'red_publications':red_publications})
    reviewers = Group.objects.get(name="Reviewers").user_set.all()
    if user in reviewers:
        return render(request,'cabinet_reviewer.html')
    files = PublicationFiles.objects.filter(author=user)
    SendFiles = files.filter(public=False)
    sc = SendFiles.count
    RightFiles = files.filter(public=True)
    rc = RightFiles.count
    return render(request,'cabinet.html',{'SendFiles':SendFiles,'sc':sc,'RightFiles':RightFiles,'rc':rc})

def filter_publications(request):
    queryset = PublicationFiles.objects.all()
    if "year" in request.GET:
        queryset = queryset.filter(
            Q(date__year__in = request.GET.getlist("year"))
        )
    if "predmet" in request.GET:
        queryset = queryset.filter(
            Q(series__name__in = request.GET.getlist("predmet"))
        )
    return render(request,'publications.html',{'files':queryset})

def filter_ajax(request):
    queryset = PublicationFiles.objects.all()
    if "year" in request.GET:
        queryset = queryset.filter(
            Q(date__year__in = request.GET.getlist("year"))
        )
    if "predmet" in request.GET:
        queryset = queryset.filter(
            Q(series__name__in = request.GET.getlist("predmet"))
        )
    queryset = queryset.distinct().values('topic','author','file')

    json_queryset = list(queryset)
    return JsonResponse({'publications':json_queryset},safe=False)

def update(request,pk):
    p = PublicationFiles.objects.get(pk=pk)
    if request.method =="POST":
        form = UpdateForm()
        form.redactor = True
        form.save()
        return redirect(p.get_absolute_url)

def api_file(request):
    files = PublicationFiles.objects.all()
    return render(request,'api_file.html',{'files':files})