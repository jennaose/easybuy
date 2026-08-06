from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


def home(request):
    return HttpResponse(
        """
        <html>
            <head><title>Easy Buy</title></head>
            <body>
                <h1>Welcome to Easy Buy</h1>
                <p>Click these links to go to these urls:</p>
                <ul>
                    <li><a href='/users/'>/users/</a> - browser user list (clickable)</li>
                    <li><a href='/api/users/'>/api/users/</a> - active users list (JSON)</li>
                    <li><a href='/api/users/profile/'>/api/users/profile/</a> - current user profile (requires auth)</li>
                    <li><a href='/api/users/register/'>/api/users/register/</a> - create a new user</li>
                    <li><a href='/api/token/'>/api/token/</a> - obtain JWT token</li>
                </ul>
            </body>
        </html>
        """,
        content_type='text/html',
    )


urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('users/', include('users.web_urls')),
    path('api/', include('listings.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/users/', include('users.urls')),
]