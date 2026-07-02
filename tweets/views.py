from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from tweets.forms import TweetForm
from tweets.models import Tweet


@login_required
def feed_view(request):
    tweets = Tweet.objects.all()

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