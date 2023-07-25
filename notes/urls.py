from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from notes import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('notes/', views.NoteList.as_view()),
    path('notes/<int:pk>/', views.NoteDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    # path('users/login/', views.Login.as_view(),name='login'),
    path('users/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),


]

urlpatterns = format_suffix_patterns(urlpatterns)