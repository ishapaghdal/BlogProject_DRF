from django.urls import path, include
from .views import BlogView, BlogFilter, PublishBlog

urlpatterns = [
    path("blogs/", BlogView.as_view()),  # post, get
    path("blogs/<int:pk>", BlogView.as_view()),  # get, put, delete
    path("blogs/filter/", BlogFilter.as_view()),  # get
    path("blogs/publish/<int:pk>", PublishBlog.as_view()),  # get
]
