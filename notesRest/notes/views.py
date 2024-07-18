from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Note
from .serializers import NoteSerializer
from django.shortcuts import get_object_or_404

# Представление для списка и создания заметок
class NoteListCreate(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

# Представление для получения информации о заметке
class NoteDetail(generics.RetrieveAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

# Представление для изменения и удаления заметки
class NoteUpdateDelete(APIView):
    def get_object(self, pk):
        return get_object_or_404(Note, pk=pk)

    def put(self, request, pk, format=None):
        note = self.get_object(pk)
        serializer = NoteSerializer(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        note = self.get_object(pk)
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
