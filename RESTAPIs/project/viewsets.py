from rest_framework import viewsets
from .import models
from .import serializers


# Create your views here.
class ProjectViewset(viewsets.ModelViewSet):
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer