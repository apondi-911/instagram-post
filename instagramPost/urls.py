"""
URL configuration for instagramPost project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from . import views as ash_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include("accounts.urls")),
    path('accounts/', include("django.contrib.auth.urls")),
    path("", TemplateView.as_view(template_name="home.html"), name='home-url'),
    path('search/', ash_views.search, name='search-url'),
    path('explore/', ash_views.explore, name='explore-url'),
    path('reels/', ash_views.reels, name='reels-url'),
    path('messages/', ash_views.messages, name='messages-url'),
    path('notifications/', ash_views.notifications, name='notifications-url'),
    path('create/', ash_views.create, name='create-url'),
    path('profile/', ash_views.profile, name='profile-url'),
    path('more/', ash_views.more, name='more-url'),
    path('accounts/login/', ash_views.login, name="login-url"),
    path('accounts/sign_up/', ash_views.sign_up, name="signUp-url")
]
