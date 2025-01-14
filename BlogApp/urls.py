from django.urls import path, include
from .views import BlogView, BlogFilter

urlpatterns = [
    path("blogs/", BlogView.as_view()),
    path("blogs/<int:pk>", BlogView.as_view()),
    path("blogs/filter/", BlogFilter.as_view()),
]
