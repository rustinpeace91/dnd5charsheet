from django.shortcuts import render
from .models import Character
# Create your views here.

def sheet(request, id):
    sheet = Character.objects.get(id=id)
    context = {
        'character': sheet
    }
    return render(request, 'charsheet.html', context)