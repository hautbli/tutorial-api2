from django.conf.urls import url
from rest_framework.authtoken import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('', include('cards.urls')),
    url('api/login/', views.obtain_auth_token)

]
