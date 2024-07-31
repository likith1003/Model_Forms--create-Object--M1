from django.shortcuts import render
from .forms import *
from django.http import HttpResponse
# Create your views here.

def register(request):
    ERFO = RegisterForm()
    d = {'ERFO': ERFO}
    if request.method == 'POST':
        name = request.POST.get('name')
        pno = request.POST.get('pno')
        email = request.POST.get('email')
        add = request.POST.get('add')
        gender=request.POST.get('gender')
        cources = request.POST.get('cources')
        un = request.POST.get('username')
        pw = request.POST.get('password')
        RFDO = RegisterForm(name=name, pno = pno, email=email, add = add, gender=gender, cources = cources, username=un, password=pw)
        RFDO.save()
    return render(request, 'register.html', d)


def insert_topic(request):
    ETFO = TopicForm()
    d = {'ETFO':ETFO}
    if request.method == 'POST':
        TFDO = TopicForm(request.POST)
        if TFDO.is_valid():
            TFDO.save()
            return HttpResponse('Topic Added')
        return HttpResponse('Invalid Data')
    return render(request, 'insert_topic.html', d)


def insert_author(request):
    EAFO = AuthorForm()
    d = {'EAFO': EAFO}
    if request.method == 'POST':
        AFDO = AuthorForm(request.POST)
        if AFDO.is_valid():
            AFDO.save()
            return HttpResponse('Author Added Successfully')
        return HttpResponse('Invalid Data')
    return render(request, 'insert_author.html', d)

def insert_book(request):
    EBFO = BookForm()
    d = {'EBFO': EBFO}
    if request.method == 'POST':
        BFDO = BookForm(request.POST)
        if BFDO.is_valid():
            BFDO.save()
            return HttpResponse('Book Added Successfully')
        return HttpResponse('Invalid Data')
    return render(request, 'insert_book.html', d)