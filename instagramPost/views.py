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


def login(request):
    return render(request, 'registration/login.html')


def sign_up(request):
    return render(request, 'registration/sign_up.html')


def msg_view(request):
    show_message = request.user.is_authenticated
    return render(request, 'home.html', {'show_message': show_message})
