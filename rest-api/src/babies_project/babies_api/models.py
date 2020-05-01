import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.

class UserProfileManager(BaseUserManager):
    '''Helps Django to work with our custom model'''

    def create_user(self, email, name, password=None):
        '''Create a new user profile object.'''

        if not email:
            raise ValueError('User must have an email address.')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, name, password):
        '''Creates and saves new superuser with given details'''

        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    '''Respents a user profile inside our system'''

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        '''Get user's full name'''
        return self.name

    def get_short_name(self):
        '''Get user's full name'''
        return self.name

    def __str__(self):
        '''To String'''
        return 'User: {}'.format(self.email)

class Baby(models.Model):
    '''Baby Model, represents a baby in our system'''
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('UserProfile', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return 'Baby: {0} Parent: {1}'.format(self.name, self.parent)

class Event(models.Model):
    '''Event Model, represents an event of a baby in our system'''
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    eType = models.CharField(max_length=100)
    eDesc = models.CharField(max_length=255)
    baby = models.ForeignKey('Baby', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return 'Event: {0} Description: {1}'.format(self.eType, self.eDesc)
