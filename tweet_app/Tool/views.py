
from django.shortcuts import render, get_object_or_404, redirect
from .models import Tweet
from .forms import Tweet_forms, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
def home(request):
    return render(request, 'home.html')

def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet_list.html', {'tweets': tweets})


@login_required
def tweet_create(request):
    if request.method == "POST":
        form = Tweet_forms(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet-list')
    else:
        form = Tweet_forms()
    
    return render(request, 'tweet_form.html', {'form': form})

@login_required
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == 'POST':
        form = Tweet_forms(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet-list')
    else:
        form = Tweet_forms(instance=tweet)
    
    return render(request, 'tweet_form.html', {'form': form})

@login_required
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('tweet-list')
    
    return render(request, 'tweet_delete.html', {'tweet': tweet})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])  # Ensure password is set correctly
            user.save()
            login(request, user)
            return redirect('tweet-list')
        else:
            print(form.errors)  # Debugging purpose to see form errors
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
 

