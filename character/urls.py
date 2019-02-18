
from django.urls import include,path
from . import views

urlpatterns = [
    path('/<int:id>/', views.sheet, name='sheet' )
]
