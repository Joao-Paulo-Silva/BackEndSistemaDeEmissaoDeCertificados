from django.shortcuts import render

from eventos.api.serializers import EventosSerializers, NomesSerializers
from rest_framework import viewsets
from .models import *
class RegisterViewSet(viewsets.ModelViewSet):
    queryset = Eventos.objects.all()
    serializer_class = EventosSerializers

class RegisterViewSetNome(viewsets.ModelViewSet):
    queryset = Nomes.objects.all()
    serializer_class = NomesSerializers