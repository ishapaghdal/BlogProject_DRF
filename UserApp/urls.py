from django.urls import path, include
from .views import UserViewSet, LoginApi

urlpatterns = [
    path('users/',UserViewSet.as_view()),
    path('users/<int:pk>',UserViewSet.as_view()),
    path('login/',LoginApi.as_view())
] 