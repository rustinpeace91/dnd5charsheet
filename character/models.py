from django.db import models
from django.contrib.auth.models import User


class Character(models.Model):
    name = models.CharField(max_length=100, unique=True)
    char_class = models.CharField(max_length=50)
    level = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='media/images', default='media/images/knight.jpg')

    strength = models.IntegerField()
    dexterity = models.IntegerField()
    constitution = models.IntegerField()
    intelligence = models.IntegerField()
    wisdom = models.IntegerField()
    charisma = models.IntegerField()

    def __str__(self):
        return self.name

class Weapon(models.Model):
    name = models.CharField(max_length=100)
    to_hit = models.IntegerField()
    damage = models.CharField(max_length=50)
    damage_type = models.CharField(max_length=50)
    weight = models.CharField(max_length=50)
    description = models.TextField()
    effects = models.TextField()
    

    def __str__(self):
        return self.name

class Spell(models.Model):
    name = models.CharField(max_length=100)
    level = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Inventory(models.Model):
    weapon = models.ForeignKey(Weapon, related_name='inventory',  on_delete=models.CASCADE)
    character = models.ForeignKey(Character, related_name='inventory',  on_delete=models.CASCADE)

class SpellBook(models.Model):
    spell = models.ForeignKey(Spell, related_name='spellbook', on_delete=models.CASCADE)
    character = models.ForeignKey(Character, related_name='spellbook',  on_delete=models.CASCADE)