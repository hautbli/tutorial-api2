from django.conf.urls import url
from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter
from django.urls import path, include
from users.views import UserViewSet, CustomAuthToken


router = SimpleRouter()
router.register(r'user', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    url(r'^api-token-auth/', views.obtain_auth_token)
]
