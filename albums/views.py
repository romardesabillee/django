from rest_framework.response import Response
from albums.models import Album
from rest_framework.viewsets import ModelViewSet

from .serializers import (
    AlbumSerializer,
)
class AlbumView(ModelViewSet):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()

    def list(self, request):
        albums = self.get_queryset()
        serializer = self.get_serializer(albums, many=True)
        return Response(serializer.data ,status=200)
    
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)