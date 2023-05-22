from rest_framework.routers import DefaultRouter
from django.urls import path

from apps.tasks.views import ToDoAPIViewSet, TasksDeleteAPIView

router = DefaultRouter()

router.register('tasks', ToDoAPIViewSet, basename='tasks')

urlpatterns = [
    path('tasks/delete/all', TasksDeleteAPIView.as_view(), name = 'delete_all_tasks')
]

urlpatterns += router.urls