from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    context = {
        'text': 'zdarova zaebal',
        'number': 100
    }
    return render(request, 'index.html', context)

def other(request):
    return render(request, 'other.html')

def relative(request):
    return render(request, 'relativeUrlTemplate.html')