from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from django.db.models import Q
import django_filters.rest_framework
from .models import Clothes
from .serializers import ClothesSerializer


class ClothesViewSet(ModelViewSet):
    serializer_class = ClothesSerializer
    queryset = Clothes.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['name', 'manufacturer']


class SomeSneakersViewSet(ReadOnlyModelViewSet):
    serializer_class = ClothesSerializer
    queryset = Clothes.objects.filter(Q(manufacturer__name='Adidas') | Q(manufacturer__name='Nike'))
