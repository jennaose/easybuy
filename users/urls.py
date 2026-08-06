from django.urls import path
from .views import ProfileView, RegisterView, UserListView

urlpatterns = [
    path('', UserListView.as_view(), name='user-list'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
]