from django.urls import path

from accounts.views import SignUpView

urlpatterns = [
    path('sign_up/', SignUpView.as_view(), name="signUp-url")

]