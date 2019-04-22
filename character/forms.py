from .models import Character, Weapon, Spell, Inventory
from django.forms import ModelForm 

class CharacterUpdateForm(ModelForm):
    class Meta:
        model = Character
        fields = (
            'name',
            'level',
            'strength',
            'dexterity',
            'constitution',
            'intelligence',
            'wisdom',
            'charisma'
        )