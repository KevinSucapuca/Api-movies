from .models import Movie
from .serializer import MovieSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    #proteger con jwt
    permission_classes = [IsAuthenticated]
    