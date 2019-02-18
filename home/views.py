from django.shortcuts import render
from django.http import HttpResponse
from character.models import Character


def index(request):
    characters = Character.objects.all()
    context = {
        'characters': characters,
        'variable': 'I am a context variable'
    }
    return render(request, 'index.html', context)