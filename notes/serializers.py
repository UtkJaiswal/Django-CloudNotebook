from rest_framework import serializers
from notes.models import Note, LANGUAGE_CHOICES, STYLE_CHOICES
from django.contrib.auth.models import User


class NoteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Note
        fields = ['id', 'title', 'desc','owner']
    

class UserSerializer(serializers.ModelSerializer):
    notes = serializers.PrimaryKeyRelatedField(many=True, queryset=Note.objects.all(),required=False)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'notes']

    def create(self, validated_data):
        password = validated_data.pop('password')
        notes_data = validated_data.pop('notes',[])  # Get the notes data from the validated data

        # Create the user object and save it to the database
        user = User(**validated_data)
        user.set_password(password)
        user.save()

        # Associate the notes with the user using the set() method
        user.notes.set(notes_data)

        return user
