from rest_framework.authentication import BasicAuthentication
from rest_framework import viewsets
from rest_framework import generics

#from rest_framework.decorators import detail_route

from django.contrib.auth.models import User, Group

from loginsys.models import *
from mobile.serializers import *
from kamera.models import *

# !!!!! AUTHENTICATION
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


# !!!!! USER !!!!!
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    def list(self,request, *args, **kwargs):
        user = getattr( self.request.user, 'username' )
        instance = User.objects.get(username = user)

        cam = User_kamera.objects.filter( user=instance )[0].kamera
        count = Bilde.objects.filter( bilde_kamera_id = cam ).count()
        args = {}
        args['count'] = count

        return Response(args)


# !!!!! Bildes !!!!!
class BildeViewSet(viewsets.ModelViewSet):
    queryset = Bilde.objects.all()
    serializer_class = BildeSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        usr = self.request.user
        cam = User_kamera.objects.filter( user=usr )[0].kamera

        args = {}
        args['user'] = str(usr)
        args['kamera'] = str(cam)

        return Bilde.objects.filter( bilde_kamera_id = cam ).order_by('-bilde_datums')
