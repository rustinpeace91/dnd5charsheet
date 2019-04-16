from django.urls import path

from .views import CharacterCollection

urlpatterns = [
    path('', CharacterCollection.as_view(), name='home'),
]