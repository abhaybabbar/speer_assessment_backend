from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.throttling import UserRateThrottle
from rest_framework import status
from .models import Note
from .serializers import NoteSerializer
from django.contrib.auth.models import User
from django.db.models import Q

class NoteListCreateView(ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]
    pagination_class = PageNumberPagination
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class NoteDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]
    
    
class ShareNoteView(CreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]

    def create(self, request, *args, **kwargs):
        note_id = self.kwargs.get('pk', None)
        shared_user_username = self.request.data.get('shared_user_username', None)

        if shared_user_username:
            try:
                note = Note.objects.get(id=note_id, user=request.user)
                shared_user = User.objects.filter(username=shared_user_username).first()
                
                if shared_user==request.user:
                    return Response({'detail': 'Cannot Share Note with self'}, status=status.HTTP_400_BAD_REQUEST)

                if shared_user:
                    if shared_user not in note.shared_with.all():
                        note.shared_with.add(shared_user)
                        note.save()
                        return Response({'detail': 'User added to shared list successfully.'}, status=status.HTTP_201_CREATED)
                    else:
                        return Response({'detail': 'User is already in the shared list.'}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({'detail': 'Invalid user username provided.'}, status=status.HTTP_400_BAD_REQUEST)

            except Note.DoesNotExist:
                return Response({'detail': 'Note not found.'}, status=status.HTTP_404_NOT_FOUND)
            
        return Response({'detail': 'shared_user_username is missing'}, status=status.HTTP_400_BAD_REQUEST)
    
    
class NoteSearchView(ListAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [UserRateThrottle]
    pagination_class = PageNumberPagination

    def get_queryset(self):
        query = self.request.query_params.get('q', None)

        if query:
            return Note.objects.filter(
                Q(title__icontains=query) | Q(content__icontains=query),
                user=self.request.user
            )

        return Note.objects.filter(user=self.request.user)