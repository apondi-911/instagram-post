from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def search(request):
    return render(request, 'search.html')


def explore(request):
    return render(request, 'explore.html')


def reels(request):
    return render(request, 'reels.html')


def messages(request):
    return render(request, 'messages.html')


def notifications(request):
    return render(request, 'notifications.html')


def create(request):
    return render(request, 'create.html')


def profile(request):
    return render(request, 'profile.html')


def more(request):
    return render(request, 'more.html')


