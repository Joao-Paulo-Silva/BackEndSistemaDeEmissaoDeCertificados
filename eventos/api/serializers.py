from rest_framework import serializers
from eventos import models

class EventosSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Eventos
        fields = '__all__'

class NomesSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Nomes
        fields = '__all__'