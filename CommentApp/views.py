from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Comment
from BlogApp.models import Blog
from .serializers import CommentSerializer

class CommentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request,pk):
        data = request.data
        user = request.user
        
        blog = get_object_or_404(Blog, id=pk, is_published=True)

        comment = Comment.objects.create(
            comment_author=user,
            blog=blog,
            comment=data.get("comment", "")
        )
        
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request, pk=None):
        if not pk:
            return Response(
                {"error": "Blog ID is required to fetch comments."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        
        blog = get_object_or_404(Blog, id=pk)
        comments = Comment.objects.filter(blog=blog)

        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        user = request.user

        comment = get_object_or_404(Comment, id=pk)
        
        if comment.blog.author == user:
            comment.delete()
            return Response(
                {"message": "Comment deleted successfully."},
                status=status.HTTP_204_NO_CONTENT,
            )
        else:
            return Response(
                {"error": "You are not authorized to delete this comment."},
                status=status.HTTP_403_FORBIDDEN,
            )
