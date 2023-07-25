from notes.models import Note
from notes.serializers import *
from rest_framework import mixins
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from notes.permissions import IsOwnerOfNote
from django.contrib.auth import authenticate, login
from django.views import View
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView


class NoteList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOfNote]
    serializer_class = NoteSerializer

    def get_queryset(self):
        # Filter notes by the currently logged-in user
        return Note.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    permission_classes = [permissions.IsAuthenticated, IsOwnerOfNote]

    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class UserList(generics.ListCreateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return User.objects.all()
        return User.objects.none()


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return User.objects.all()
        return User.objects.none()

   
class Login(generics.ListCreateAPIView):
    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")
        print("username",request.POST)
        print("password",password)
        if username and password:
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                # Redirect to a success page.
                return JsonResponse({"message": "Login successful"})
            else:
                # Return an 'invalid login' error message.
                return JsonResponse({"error": "Invalid credentials"}, status=401)
        else:
            return HttpResponseBadRequest("Both 'username' and 'password' are required.")

