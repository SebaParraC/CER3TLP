from django.urls import path, include
from rest_framework import routers
from . import views
from .views import LibroViewSet

router = routers.DefaultRouter()
router.register('libros',views.LibroViewSet)

urlpatterns= [
    path('',include(router.urls))
]