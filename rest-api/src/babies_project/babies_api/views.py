from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from . import models
from . import serializers
from . import permissions

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    '''Handles creating, reading and updating user profiles'''

    queryset = models.UserProfile.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [
        permissions.APIPermissionClassFactory(
            name='UserPermissions',
            permission_configuration={
                'base': {
                    'create': True,
                    'list': True,
                    'update': False,
                    'partial_update': False,
                },
                'instance': {
                    'retrieve': False,
                    'destroy': True,
                    'update': False,
                }
            }
        )
    ]

class BabyViewSet(viewsets.ModelViewSet):
    '''Handles creating, reading and updating babies'''

    queryset = models.Baby.objects.all()
    serializer_class = serializers.BabySerializer
    permission_classes = [
        permissions.APIPermissionClassFactory(
            name='BabyPermissions',
            permission_configuration={
                'base': {
                    'create': True,
                    'list': True,
                    'update': False,
                    'partial_update': False,
                },
                'instance': {
                    'retrieve': False,
                    'destroy': True,
                    'update': False,
                }
            }
        )
    ]
    

class EventViewSet(viewsets.ModelViewSet):
    '''Handles creating, reading and updating events'''

    queryset = models.Event.objects.all()
    serializer_class = serializers.EventSerializer
    permission_classes = [
        permissions.APIPermissionClassFactory(
            name='EventPermissions',
            permission_configuration={
                'base': {
                    'create': True,
                    'list': True,
                    'update': False,
                    'partial_update': False,
                },
                'instance': {
                    'retrieve': False,
                    'destroy': True,
                    'update': False,
                }
            }
        )
    ]