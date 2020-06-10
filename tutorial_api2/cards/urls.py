from django.conf.urls import url
from rest_framework.routers import SimpleRouter
from django.urls import path, include
from cards.views import CardViewSet

router = SimpleRouter()
router.register(r'card', CardViewSet, basename='card')

urlpatterns = [
    path('', include(router.urls)),
]
