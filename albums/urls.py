from django.urls import path, include
from .views import (
    AlbumView,
)
 
urlpatterns = [
    path('', AlbumView.as_view({
        'get': 'list',
        'post': 'create',
    }))
]