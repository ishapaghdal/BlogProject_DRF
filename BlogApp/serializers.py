from rest_framework import serializers
from .models import Blog, Tag, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
        )


class TagSerializer(serializers.ModelSerializer):
    # blog_list = BlogSerializer(many=True, read_only=True)
    class Meta:
        model = Tag
        fields = (
            "id",
            "name",
        )


class BlogSerializer(serializers.ModelSerializer):

    comment_count = serializers.SerializerMethodField()
    # tags = serializers.ListField(child=serializers.CharField(max_length=20),write_only=True)
    tags = TagSerializer(read_only=True, many=True)

    class Meta:
        model = Blog
        fields = (
            "title",
            "publication_date",
            "author",
            "content",
            "category",
            "tags",
            "is_published",
            "comment_count",
        )
        read_only_fields = (
            "author",
            "comments",
        )
        depth = 1

    def get_comment_count(self, obj):
        return obj.comments.count()

    def create(slef, validated_data):
        tags_data = validated_data.pop("tags", [])
        category_data = validated_data.pop("category")

        category = Category.objects.get_or_create(name=category_data["name"])

        blog = Blog.objects.create(category=category, **validated_data)

        for tag in tags_data:
            Tag.objects.get_or_create(name=tag["name"])
            blog.tags.add(tag)
