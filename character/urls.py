
from django.urls import include, path
from .views import CharSheetView, CharacterCreateView

urlpatterns = [
    path('<int:id>/', CharSheetView.as_view(), name='sheet' ),
    path('add/', CharacterCreateView.as_view(), name='add_character')

]
