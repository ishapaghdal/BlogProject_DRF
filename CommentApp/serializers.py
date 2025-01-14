from rest_framework import serializers

from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    comment_author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = [
            "id",
            "comment_author",
            "blog",
            "comment",
        ]
        extra_kwargs = {
            "blog": {"write_only": True}, 
        }