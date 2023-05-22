from django.urls import path

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.users.views import UserAPIViewSet

router = DefaultRouter()

router.register('users', UserAPIViewSet, basename='users')


urlpatterns = [
    path('users/login/', TokenObtainPairView.as_view(), name = 'api_login'),
    path('users/refresh/', TokenRefreshView.as_view(), name = 'api_refresh'),
]
urlpatterns += router.urls