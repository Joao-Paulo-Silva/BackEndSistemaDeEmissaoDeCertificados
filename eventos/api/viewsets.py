from rest_framework import viewsets
from eventos import models
from eventos.api import serializers

class EventosViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.EventosSerializers
    queryset = models.Eventos.objects.all()

class NomesViewSets(viewsets.ModelViewSet):
    serializer_class = serializers.NomesSerializers
    queryset = models.Nomes.objects.all()