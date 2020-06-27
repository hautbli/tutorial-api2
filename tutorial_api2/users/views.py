from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
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

    @method_decorator(cache_page(60 * 60 * 2))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(60 * 60 * 2))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
