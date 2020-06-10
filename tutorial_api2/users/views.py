from django.contrib.auth.models import User
from rest_framework import viewsets, status
# from users.models import User
from rest_framework.pagination import CursorPagination
from rest_framework.permissions import IsAuthenticated

from users.permissions import IsOwnerOrReadOnly
from users.serializers import UserSerializer


class UserPagination(CursorPagination):
    ordering = '-id'

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = UserPagination
    permission_classes = [IsAuthenticated,
                          IsOwnerOrReadOnly]

