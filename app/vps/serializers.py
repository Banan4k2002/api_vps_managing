from rest_framework import serializers

from vps.models import VPS


class VPSSerializer(serializers.ModelSerializer):

    class Meta:
        model = VPS
        fields = ('uid', 'cpu', 'ram', 'hdd', 'status')


class ChangeStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = VPS
        fields = ('uid', 'cpu', 'ram', 'hdd', 'status')
        read_only_fields = ('uid', 'cpu', 'ram', 'hdd')
