from rest_framework import viewsets, status
from rest_framework.pagination import CursorPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response

from cards.models import Card
from cards.permissions import IsOwnerOrReadOnly
from cards.serializers import CardSerializer

class CardPagination(CursorPagination):
    ordering = '-id'

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    pagination_class =CardPagination

    # permission_classes = [IsAuthenticatedOrReadOnly, ]
    permission_classes = [IsAuthenticated,
                          IsOwnerOrReadOnly]


    def create(self, request, *args, **kwargs):
        request.data['user'] = request.user.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)