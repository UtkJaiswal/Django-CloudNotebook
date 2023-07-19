from rest_framework import serializers
from notes.models import Note, LANGUAGE_CHOICES, STYLE_CHOICES


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'title', 'desc']
    