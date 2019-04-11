from django.contrib import admin
from .models import Character, Weapon, Spell, Inventory



class CharacterAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            'Info', {
                'fields': (
                    'name',
                    'char_class',
                    'level',
                    'image',
                    'description'

                )
            }
        ),
        (
            'Stats', {
                'fields': (
                    'strength',
                    'dexterity',
                    'constitution',
                    'intelligence',
                    'wisdom',
                    'charisma'
                )
            }
        )
    )

# Register your models here.
admin.site.register(Character, CharacterAdmin);
admin.site.register(Weapon);
admin.site.register(Spell);
admin.site.register(Inventory);