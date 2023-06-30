from django.shortcuts import render
from rest_framework import viewsets
from .serializer import LibroSerializer
from Libros.models import Libro
# Create your views here.

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
