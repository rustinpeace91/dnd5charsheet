from django.shortcuts import render
from . import models
# Create your views here.

def sheet(request, id):
    sheet = Character.objects.get(id=id)
    context = {
        'character': sheet
    }
    return('charsheet.html', context)