from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Note
from .serializers import NoteSerializer


@api_view(['GET']) # endpoint obsługuje tylko get
@permission_classes([IsAuthenticated]) #zalogowny użytkownik
def notes_list_api(request):
    notes = Note.objects.filter(owner=request.user).order_by('-is_pinned', '-updated_at')
    serializer = NoteSerializer(notes, many=True) # konwersja na JSON
    return Response(serializer.data) # zwraca liste notatek w JSON


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def note_detail_api(request, pk): # pk - id notatki
    try:
        note = Note.objects.get(pk=pk, owner=request.user)
    except Note.DoesNotExist: # nie ma notatki lub nie należy do zalogowanego uż
        return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)

    serializer = NoteSerializer(note)
    return Response(serializer.data) # zwraca notatke
