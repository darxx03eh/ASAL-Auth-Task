from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from api.views.user_views import SignUpAPIView, LogOutAPIView, UserAPIView, UserRetrieveAPIView

urlpatterns = [
    path('users/me', UserRetrieveAPIView.as_view(), name='retrieve-user'),
    path('users', UserAPIView.as_view(), name='users'),
    path('users/signup', SignUpAPIView.as_view(), name='signup'),
    path('users/login', TokenObtainPairView.as_view(), name='login'),
    path('users/logout', LogOutAPIView.as_view(), name='logout'),
    path('users/refresh', TokenRefreshView.as_view(), name='refresh'),
]
