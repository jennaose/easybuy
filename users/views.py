from rest_framework import generics, permissions
from .models import User
from .serializers import UserProfileSerializer, UserRegisterSerializer

from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404


class RegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]


class UserListView(generics.ListAPIView):
    """List active users."""
    queryset = User.objects.filter(is_active=True).order_by('id')
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.AllowAny]


class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


# --- Browser-friendly (non-API) views for clickable links ---
class UserListPageView(ListView):
    model = User
    template_name = 'users/user_list.html'
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.filter(is_active=True).order_by('id')


class UserDetailPageView(DetailView):
    model = User
    template_name = 'users/user_detail.html'
    context_object_name = 'user_obj'

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return get_object_or_404(User, pk=pk, is_active=True)