from django.urls import path, include
from .views import BlogView

urlpatterns = [
    path('blogs/',BlogView.as_view()),
] 