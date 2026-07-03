from rest_framework import serializers

from tweets.models import Comment, Tweet


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = ["id", "author", "content", "created_at"]


class TweetSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    comments = CommentSerializer(many=True, read_only=True)
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Tweet
        fields = [
            "id",
            "author",
            "content",
            "likes_count",
            "comments",
            "created_at",
            "updated_at",
        ]

    def get_likes_count(self, obj):
        return obj.likes.count()
