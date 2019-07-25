from django.urls import path

from .views import CharacterCollection, api_get_characters

urlpatterns = [
    path('', CharacterCollection.as_view(), name='home'),
    path('api/characters', api_get_characters, name='api')
]