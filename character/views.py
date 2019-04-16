from django.shortcuts import render
from .models import Character, Weapon, Spell, Inventory
from django.views.generic.base import TemplateView

# Create your views here.

class CharSheetView(TemplateView):
    template_name = 'charsheet.html'

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        char_id = self.kwargs['id']
        character = Character.objects.get(id=char_id)
        stats = {
            "strength":character.strength,
            "dexterity":character.dexterity,
            "constitution":character.constitution,
            "intelligence":character.intelligence,
            "wisdom":character.wisdom,
            "charisma":character.charisma
        }

        inventory = Inventory.objects.filter(character=char_id)

        context_vars = {
            'character': character,
            'stats':stats,
            'inventory': inventory,
        }
        context.update(context_vars)
        return context
    
