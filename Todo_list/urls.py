from django.urls import path
from rest_framework import routers
from .views import TodoViewset

router = routers.DefaultRouter()
router.register('api', TodoViewset)

