from rest_framework import generics, permissions
from .models import User
from .serializers import UserProfileSerializer, UserRegisterSerializer

from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404

def get_user_queryset(request):
    include_inactive = request.GET.get('include_inactive', '').lower() in('1', 'true', 'yes')
    queryset = User.objects.all() if include_inactive else User.objects.filter(is_active=True)
    return queryset.order_by('id')

class RegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [permissions.AllowAny]

class UserListView(generics.ListAPIView):
    """List users; by default only active users. Pass ?include_inactive=1 to include inactive users."""
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        include_inactive = str(self.request.GET.get('include_inactive', '')).lower() in ('1', 'true', 'yes')
        qs = User.objects.all() if include_inactive else User.objects.filter(is_active=True)
        return qs.order_by('id')


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
        include_inactive = str(self.request.GET.get('include_inactive', '')).lower() in ('1', 'true', 'yes')
        qs = User.objects.all() if include_inactive else User.objects.filter(is_active=True)
        return qs.order_by('id')


class UserDetailPageView(DetailView):
    model = User
    template_name = 'users/user_detail.html'
    context_object_name = 'user_obj'

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return get_object_or_404(User, pk=pk, is_active=True)