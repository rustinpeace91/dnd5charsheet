from django.urls import path

from .views import PostCollection

urlpatterns = [
    path('', PostCollection.as_view(), name='home')
]