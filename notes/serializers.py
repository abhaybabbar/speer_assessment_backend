from rest_framework import serializers
from .models import Note
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']
        
class NoteSerializer(serializers.ModelSerializer):
    shared_with = UserSerializer(many=True, read_only=True)
    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'shared_with']