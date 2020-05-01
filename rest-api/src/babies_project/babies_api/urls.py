from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register('profile', views.UserViewSet)
router.register('baby', views.BabyViewSet)
router.register('event', views.EventViewSet)

#TODO add path
urlpatterns = [
    path(r'', include(router.urls))
]