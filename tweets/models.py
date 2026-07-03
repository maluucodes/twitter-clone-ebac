from django.contrib.auth.models import User
from django.db import models


class Tweet(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tweets")
    content = models.TextField(max_length=280)
    likes = models.ManyToManyField(User, related_name="liked_tweets", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.author.username}: {self.content[:30]}"


class Comment(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField(max_length=280)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"{self.author.username}: {self.content[:30]}"
