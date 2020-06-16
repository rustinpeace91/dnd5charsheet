
from django.urls import include, path
from .views import CharSheetView, CharacterCreateView, CharacterUpdateView
urlpatterns = [
    path('<int:id>/', CharSheetView.as_view(), name='sheet' ),
    path('add/', CharacterCreateView.as_view(), name='add_character'),
    path('update/<int:pk>/', CharacterUpdateView.as_view(), name='character_update')
]
