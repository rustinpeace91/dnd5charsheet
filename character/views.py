from django.shortcuts import render
from .models import Character, Weapon, Spell, Inventory
from django.views.generic.base import TemplateView

from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
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
    
class CharacterCreateView(LoginRequiredMixin, CreateView):
    template_name = 'character_form.html'
    model = Character
    fields = [
        'name',
        'char_class',
        'level',
        'description',
        'image',
        'strength',
        'dexterity',
        'constitution',
        'intelligence',
        'wisdom',
        'charisma'
    ]

class CharacterUpdateView(LoginRequiredMixin, UpdateView):
    model = Character
    fields = [
        'name',
        'char_class',
        'level',
        'description',
        'image',
        'strength',
        'dexterity',
        'constitution',
        'intelligence',
        'wisdom',
        'charisma'
    ]

    # steps
        #takes in data and model
        # sends pk, data to update form
        # returns response 