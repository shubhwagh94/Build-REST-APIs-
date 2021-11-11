from rest_framework import viewsets
from .import models
from .import serializers


# Create your views here.
class ClientViewset(viewsets.ModelViewSet):
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer