from django.urls import path, include
from .views import BlogView, BlogFilter,PublishBlog

urlpatterns = [
    path("blogs/", BlogView.as_view()),
    path("blogs/<int:pk>", BlogView.as_view()),
    path("blogs/filter/", BlogFilter.as_view()),
    path("blogs/publish/<int:pk>",PublishBlog.as_view()),
]
