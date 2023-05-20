from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from apps.tasks.models import ToDo
from apps.tasks.serializer import ToDoSerializer
# Create your views here.

class ToDoAPIViewSet(GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer