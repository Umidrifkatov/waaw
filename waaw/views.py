from django.shortcuts import render
from .models import *

def home(request):
    return render(request, 'base.html', {})

def contest(request):
    return render(request, 'contest.html', {})

def plan(request):
    return render(request, 'plan.html', {})

def more(request):
    return render(request, 'more.html', {})

def contestlive(request):
    content = Contest.objects.filter(active=True)
    return render(request, 'contestlive.html', {"contest":content})
