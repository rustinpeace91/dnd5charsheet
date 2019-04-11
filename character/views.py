from django.shortcuts import render
from .models import Character, Weapon, Spell, Inventory
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

    inventory = Inventory.objects.filter(character=id)
    

    context = {
        'character': character,
        'stats':stats,
        'inventory': inventory,
    }
    return render(request, 'charsheet.html', context)