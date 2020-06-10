
from rest_framework.routers import SimpleRouter
from django.urls import path, include
from users.views import UserViewSet


router = SimpleRouter()
router.register(r'user', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]
