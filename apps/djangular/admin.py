from django.contrib import admin
from rest_framework import routers
from . import views
# Register your models here.
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)