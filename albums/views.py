from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .serializers import (
    AlbumSerializer,
)
from .models import Album

class AlbumView(ModelViewSet):
    serializer_class = AlbumSerializer

    def get_queryset(self):
        return Album.objects.all()

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = AlbumSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)