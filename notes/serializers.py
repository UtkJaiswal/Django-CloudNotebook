from rest_framework import serializers
from notes.models import Note, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User


class NoteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Note
        fields = ['id', 'title', 'desc','owner']
    
class UserSerializer(serializers.ModelSerializer):
    notes = serializers.PrimaryKeyRelatedField(many=True, queryset=Note.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'notes']