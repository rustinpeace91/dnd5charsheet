from .models import Character
from django.forms import ModelForm 
from django.core.exceptions import ValidationError
class CharacterUpdateForm(ModelForm):

    def clean(self):
        cleaned_data = super().clean()


    class Meta:
        model = Character
        fields = (
            'name',
            'level', 
            'char_class',
            'description'
        )