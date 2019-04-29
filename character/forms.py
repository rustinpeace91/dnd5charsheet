from .models import Character, Weapon, Spell, Inventory
from django.forms import ModelForm 
from django.core.exceptions import ValidationError
class CharacterUpdateForm(ModelForm):

    def clean(self):
        cleaned_data = super().clean()
        stats = [
            'strength', 
            'dexterity', 
            'constitution', 
            'intelligence', 
            'wisdom', 
            'charisma' 
        ]
        # not needed yet, but will be useful for custom error handling 
        for stat in stats:
            if stat not in cleaned_data:
                pass

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