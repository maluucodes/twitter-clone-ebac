from django.urls import path

from tweets.views import delete_tweet_view, edit_tweet_view, feed_view, like_tweet_view, comment_tweet_view


urlpatterns = [
    path("", feed_view, name="feed"),
    path("tweets/<int:tweet_id>/editar/", edit_tweet_view, name="edit_tweet"),
    path("tweets/<int:tweet_id>/deletar/", delete_tweet_view, name="delete_tweet"),
    path("tweets/<int:tweet_id>/curtir/", like_tweet_view, name="like_tweet"),
    path("tweets/<int:tweet_id>/comentar/", comment_tweet_view, name="comment_tweet"),
]