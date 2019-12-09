from django.shortcuts import render
from django.http import HttpResponse
from .models import About, Project

def homepage(request):
    print('---------- viewing Homepage')
    cards = []
    for about in About.objects.all(): 
        cards.append({
            'title': about.title,
            'sub_title_1': about.sub_title_1,
            'sub_title_2': about.sub_title_2,
            'content_1': about.content_1,
            'content_2': about.content_2,
        })
    context = {
        'title': 'about',
        'path': '/', 
        'cards': cards,
        'pages': pages(),
    }
    return render(request, 'pages/homepage.html', context)

def projects(request):
    print('---------- viewing Projects')
    cards = []
    for project in Project.objects.all(): 
        cards.append({
            'title': project.title,
            'sub_title': project.sub_title,
            'link': project.link,
            'image': project.image,
        })
    context = {
        'title': 'projects',
        'path': 'projects', 
        'cards': cards,
        'pages': pages(),
    }
    return render(request, 'pages/projects.html', context)

def pages(): 
    return [
        {'title': 'about', 'path': '/'}, 
        {'title': 'projects', 'path': 'projects'}, 
    ]