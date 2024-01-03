from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']
        
        
class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    
    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)
        
        if username is None or password is None:
            raise serializers.ValidationError('Both username and password are required for login.')

        user = User.objects.filter(username=username).first()

        if user is None or not user.check_password(password):
            raise serializers.ValidationError('Invalid username or password.')

        refresh = RefreshToken.for_user(user)
        data['access_token'] = str(refresh.access_token)
        data['refresh_token'] = str(refresh)
        
        # Exclude password from the response
        del data['password']

        return data