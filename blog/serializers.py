from rest_framework import serializers
from .models import Note


# Serializer dla modelu Note: zamienia obiekt Note (z bazy) -> JSON
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        # jakie pola mają znaleźć się w JSON
        fields = ['id', 'title', 'content', 'priority', 'is_pinned', 'due_date', 'category', 'updated_at']
