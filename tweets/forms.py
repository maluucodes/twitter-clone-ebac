from django import forms

from tweets.models import Comment, Tweet


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ["content"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
