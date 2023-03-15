from django.contrib.auth.models import User
from .serializer import UserSerializer
from rest_framework import viewsets
#HASHEAR PASSWORD
from django.contrib.auth.hashers import make_password

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #HASHEAR PASSWORD
    def perform_create(self, serializer):
        serializer.save(password=make_password(serializer.validated_data['password']))
        