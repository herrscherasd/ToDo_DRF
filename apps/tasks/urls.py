from rest_framework.routers import DefaultRouter

from apps.tasks.views import ToDoAPIViewSet

router = DefaultRouter()

router.register('tasks', ToDoAPIViewSet, basename='tasks')

urlpatterns = router.urls