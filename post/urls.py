
from django.urls import include, path
from .views import PostsheetView, PostCreateView, PostUpdateView
urlpatterns = [
    path('<int:id>/', PostsheetView.as_view(), name='sheet' ),
    path('add/', PostCreateView.as_view(), name='add_Post'),
    path('update/<int:pk>/', PostUpdateView.as_view(), name='Post_update')
]
