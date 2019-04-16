
from django.urls import include, path
from .views import CharSheetView

urlpatterns = [
    path('<int:id>/', CharSheetView.as_view(), name='sheet' )
]
