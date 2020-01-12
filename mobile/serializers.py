from django.contrib.auth.models import User, Group
from rest_framework import serializers

from kamera.models import *
from loginsys.models import User_kamera


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'url')

# !!!!! KAMERA !!!!!
class KameraSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Kamera
        fields = ('kamera_nos', 'kamera_slug', 'kamera_type')

# !!!!! USER - KAMERA !!!!!
class User_kameraSerializer(serializers.HyperlinkedModelSerializer):
    kamera = KameraSerializer(many=False)

    class Meta:
        model = User_kamera
        fields = ('id', 'kamera')


class BildeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bilde
        fields = ('bilde_thumb', 'bilde_bilde', 'bilde_datums')
