from django.shortcuts import render
from .models import Character
# Create your views here.

def sheet(request, id):
    character = Character.objects.get(id=id)
    stats = {
        "strength":character.strength,
        "dexterity":character.dexterity,
        "constitution":character.constitution,
        "intelligence":character.intelligence,
        "wisdom":character.wisdom,
        "charisma":character.charisma
    }
    context = {
        'character': character,
        'stats':stats
    }
    return render(request, 'charsheet.html', context)