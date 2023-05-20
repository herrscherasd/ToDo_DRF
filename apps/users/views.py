from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins


from apps.users.models import User
from apps.users.serializer import UserSerializer
# Create your views here.

class UserAPIViewSet(GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer