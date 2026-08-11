from django.shortcuts import render


def home_view(request):
    return render(request, 'portfolio/index.html')

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def skills(request):
    return render(request, 'skills.html')


def projects(request):
    return render(request, 'projects.html')


def contact(request):
    return render(request, 'contact.html')