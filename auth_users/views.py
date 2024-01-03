from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserRegistrationSerializer, UserLoginSerializer


class UserRegistrationView(CreateAPIView):
    serializer_class = UserRegistrationSerializer

class UserLoginView(TokenObtainPairView):
    serializer_class = UserLoginSerializer