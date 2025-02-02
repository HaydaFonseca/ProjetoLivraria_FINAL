from rest_framework.viewsets import ModelViewSet

from core.models import Favorito
from core.serializers import FavoritoSerializer


class FavoritoViewSet(ModelViewSet):
    queryset = Favorito.objects.order_by("-id")
    serializer_class = FavoritoSerializer
