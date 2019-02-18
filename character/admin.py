from django.contrib import admin
from .models import Character, Weapon, Spell

# Register your models here.
admin.site.register(Character);
admin.site.register(Weapon);
admin.site.register(Spell);