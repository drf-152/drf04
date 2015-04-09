from rest_framework import permissions
from rest_framework.generics import ListAPIView

from core.models import AAAA

from .serializers import AAAASerializer


class AAAAFeedView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = AAAA.objects.all()
    serializer_class = AAAASerializer
