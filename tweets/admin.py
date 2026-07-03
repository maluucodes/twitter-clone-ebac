from django.contrib import admin

from tweets.models import Comment, Tweet


@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ("author", "content", "created_at")
    search_fields = ("author__username", "content")
    list_filter = ("created_at",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("author", "tweet", "content", "created_at")
    search_fields = ("author__username", "content")