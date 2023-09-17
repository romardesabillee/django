from django.urls import path
from .views import AlbumView

urlpatterns = [
    path('', AlbumView.as_view({
        'get': 'list',
        'post': 'create',
    }))
]
