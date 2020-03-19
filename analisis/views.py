from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'analisis/index.html')

def crawling(request):
    return HttpResponse('ini crawling')

def preprocessing(request):
    return HttpResponse('ini preprocessing')

def classification(request):
    return HttpResponse('ini classification')

def visualization(request):
    return HttpResponse('ini visualization')