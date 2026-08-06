from django.urls import path
from .views import UserListPageView, UserDetailPageView

urlpatterns = [
    path('', UserListPageView.as_view(), name='web-user-list'),
    path('<int:pk>/', UserDetailPageView.as_view(), name='web-user-detail'),
]
