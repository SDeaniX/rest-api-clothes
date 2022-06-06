from rest_framework.routers import DefaultRouter
from django.contrib import admin
from django.urls import path, include

from api.views import ClothesViewSet, SomeSneakersViewSet
from user.views import UserViewSet

router = DefaultRouter()
router.register('clothes', ClothesViewSet, basename='clothes')
router.register('user', UserViewSet)
router.register('sneakers', SomeSneakersViewSet, basename='sneakers')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
