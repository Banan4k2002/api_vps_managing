from rest_framework.viewsets import ModelViewSet

from vps.serializers import ChangeStatusSerializer, VPSSerializer
from vps.models import VPS


class VPSViewSet(ModelViewSet):
    """Работа с виртуальными серверами."""
    queryset = VPS.objects.all()
    serializer_class = VPSSerializer
    http_method_names = ['get', 'post', 'patch']

    def get_serializer_class(self):
        if self.action == 'partial_update':
            return ChangeStatusSerializer
        return super().get_serializer_class()
