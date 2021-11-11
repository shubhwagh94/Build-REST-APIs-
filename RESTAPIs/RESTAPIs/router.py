from client.viewsets import ClientViewset
from project.viewsets import ProjectViewset
from user.viewsets import UserViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('client',ClientViewset)
router.register('project', ProjectViewset)
router.register('user',UserViewset)