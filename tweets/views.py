from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from tweets.forms import CommentForm, TweetForm
from tweets.models import Tweet


@login_required
def feed_view(request):
    following_profiles = request.user.profile.following.all()
    following_users = [profile.user for profile in following_profiles]

    following_users.append(request.user)

    tweets = Tweet.objects.filter(author__in=following_users)

    if request.method == "POST":
        form = TweetForm(request.POST)

        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.author = request.user
            tweet.save()
            return redirect("feed")
    else:
        form = TweetForm()

    return render(request, "tweets/feed.html", {"tweets": tweets, "form": form})


@login_required
def edit_tweet_view(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id, author=request.user)

    if request.method == "POST":
        form = TweetForm(request.POST, instance=tweet)

        if form.is_valid():
            form.save()
            return redirect("feed")
    else:
        form = TweetForm(instance=tweet)

    return render(request, "tweets/edit_tweet.html", {"form": form})


@login_required
def delete_tweet_view(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id, author=request.user)

    if request.method == "POST":
        tweet.delete()
        return redirect("feed")

    return render(request, "tweets/delete_tweet.html", {"tweet": tweet})


@login_required
def like_tweet_view(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)

    if request.user in tweet.likes.all():
        tweet.likes.remove(request.user)
    else:
        tweet.likes.add(request.user)

    return redirect("feed")


@login_required
def comment_tweet_view(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id)

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.tweet = tweet
            comment.author = request.user
            comment.save()

    return redirect("feed")