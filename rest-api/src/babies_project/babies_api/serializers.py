from rest_framework import serializers

from . import models

class UserSerializer(serializers.ModelSerializer):
    '''Serializer for user object'''

    class Meta:
        model = models.UserProfile
        fields = (
            'id',
            'email',
            'name',
            'password'
        )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        '''Create and return a new user'''
        
        user = models.UserProfile(
            email=validated_data['email'],
            name=validated_data['name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

class BabySerializer(serializers.ModelSerializer):
    '''Serializer for baby object'''

    class Meta:
        model = models.Baby
        fields = (
            'id',
            'name',
            'parent'
        )

    def create(self, validated_data):
        '''Create and return a new baby'''
        
        baby = models.Baby(
            name=validated_data['name'],
            parent=validated_data['parent']
        )

        baby.save()

        return baby

class EventSerializer(serializers.ModelSerializer):
    '''Serializer for event object'''

    class Meta:
        model = models.Event
        fields = (
            'id',
            'eType',
            'eDesc',
            'baby'
        )

    def create(self, validated_data):
        '''Create and return a new event'''
        
        event = models.Event(
            eType=validated_data['eType'],
            eDesc=validated_data['eDesc'],
            baby=validated_data['baby']
        )

        event.save()

        return event