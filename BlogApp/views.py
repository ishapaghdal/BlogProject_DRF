from django.shortcuts import render
from .serializers import BlogSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.utils.timezone import now
from .models import Blog, Tag, Category
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class BlogView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        user = request.user

        title = data.get("title")
        content = data.get("content")
        publication_date = now().date()  if data.get("is_published", False) else None
        category_data = data.get("category")
        tags_data = data.get("tags", [])

        category = None
        if category_data:
            category, _ = Category.objects.get_or_create(name=category_data)

        blog = Blog.objects.create(
            title=title,
            content=content,
            publication_date=publication_date,
            author=user,
            category=category,
            is_published=data.get("is_published", False),
        )

        tag_instances = []
        for tag_name in tags_data:
            tag, _ = Tag.objects.get_or_create(name=tag_name)
            tag_instances.append(tag)

        blog.tags.set(tag_instances)

        serializer = BlogSerializer(blog)
        return Response(serializer.data, status=201)
    
    def get(self, request, pk=None):
        if pk:
            blog = get_object_or_404(Blog, id=pk)
            serializer = BlogSerializer(blog)
            return Response(serializer.data, status=200)
        else:
            blogs = Blog.objects.filter(is_published=True)
            serializer = BlogSerializer(blogs, many=True)
            return Response(serializer.data, status=200)

