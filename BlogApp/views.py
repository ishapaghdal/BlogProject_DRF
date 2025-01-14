from django.shortcuts import render
from .serializers import BlogSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.utils.timezone import now
from .models import Blog, Tag, Category
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from django.db.models import Count
from django.db.models import Q


class BlogView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        user = request.user

        title = data.get("title")
        content = data.get("content")
        publication_date = now().date() if data.get("is_published", False) else None
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

    def put(self, request, pk):
        user = request.user
        data = request.data

        try:
            # Fetch the blog instance
            blog = Blog.objects.get(id=pk, author=user)

            # Update the blog details
            blog.title = data.get("title", blog.title)
            blog.content = data.get("content", blog.content)
            blog.is_published = data.get("is_published", blog.is_published)
            blog.publication_date = now().date()
            blog.save()

            return Response(
                {
                    "success": True,
                    "message": "Blog updated successfully",
                    "blog": {
                        "id": blog.id,
                        "title": blog.title,
                        "content": blog.content,
                        "is_published": blog.is_published,
                        "publication_date": blog.publication_date,
                        # 'comments': blog.comments_set.count()
                    },
                },
                status=200,
            )
        except Blog.DoesNotExist:
            return Response(
                {"success": False, "message": "Blog not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

    def delete(self, request, pk):
        user = request.user

        try:
            blog = Blog.objects.filter(id=pk, author=user)

            if not blog:
                return Response({"success": False, "message": "Blog does not exist"})

            blog.delete()

            return Response({"success": True, "message": "Blog Deleted Successfully"})
        except Blog.DoesNotExist:
            return Response(
                {"success": False, "message": "Blog not found or unauthorized access."},
                status=status.HTTP_404_NOT_FOUND,
            )


class BlogFilter(ListAPIView):
    def get(self, request):
        author = request.query_params.get("author")
        category = request.query_params.get("category")
        tags = request.query_params.getlist("tags")
        search_query = request.query_params.get("search")

        queryset = Blog.objects.filter(is_published=True)

        if author:
            queryset = queryset.filter(author__id=author)
        if category:
            queryset = queryset.filter(category__id=category)
        if tags:
            queryset = queryset.filter(tags__id__in=tags).distinct()
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query)
                | Q(content__icontains=search_query)
                | Q(category__name__icontains=search_query)
                | Q(tags__name__icontains=search_query)
                | Q(author__username__icontains=search_query)
            )

        # Pagination
        paginator = PageNumberPagination()
        paginator.page_size = 10
        paginated_queryset = paginator.paginate_queryset(queryset, request)

        # Serialize data
        serializer = BlogSerializer(paginated_queryset, many=True)

        # Return paginated response
        return paginator.get_paginated_response(serializer.data)
