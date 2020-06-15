from django.contrib import admin
from .models import Character



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
    )

# Register your models here.
admin.site.register(Character, CharacterAdmin)
