from django.shortcuts import render

def home(request):
    return render(request, 'base.html', {})

def contest(request):
    return render(request, 'contest.html', {})

def plan(request):
    return render(request, 'plan.html', {})

def more(request):
    return render(request, 'more.html', {})
