from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import mixins, generics

from apps.tasks.models import ToDo
from apps.tasks.permission import TaskPermission
from apps.tasks.serializer import ToDoSerializer, TaskDetailSerializer
# Create your views here.

class ToDoAPIViewSet(GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

    def get_serializer_class(self):
        if self.action in ('retrieve', ):
            return TaskDetailSerializer
        return ToDoSerializer

    def get_permissions(self):
        if self.action in ('create', 'retrieve', 'partial_update', 'update', 'destroy', 'list'):
            return (TaskPermission(), IsAuthenticated())
        return (AllowAny(), )
    
class TasksDeleteAPIView(generics.DestroyAPIView):
    serializer_class = TaskDetailSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return ToDo.objects.filter(user_id=user_id)