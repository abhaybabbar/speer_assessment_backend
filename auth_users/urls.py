from django.urls import path
from .views import UserLoginView, UserRegistrationView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('signup/', UserRegistrationView.as_view(), name='user_signup'),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
