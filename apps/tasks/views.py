from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import mixins, generics
from rest_framework import filters

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
    filter_backends = [filters.SearchFilter]
    search_fields = ('title', 'description')


    def get_serializer_class(self):
        if self.action in ('retrieve', ):
            return TaskDetailSerializer
        return ToDoSerializer

    def get_permissions(self):
        if self.action in ('create', 'retrieve', 'partial_update', 'update', 'destroy', 'list'):
            return (TaskPermission(), IsAuthenticated())
        return (AllowAny(), )
    
class TasksDeleteAPIView(generics.DestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    permission_classes = (TaskPermission, )

    def delete(self,request, *args, **kwargs):
        todo = ToDo.objects.filter(user = request.user)
        todo = [i for i in todo.delete()]

        return Response({"delete": "Все таски удалены"})