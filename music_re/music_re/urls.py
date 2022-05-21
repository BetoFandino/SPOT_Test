from django.contrib import admin
from django.urls import path, include
from login.views import login

urlpatterns = [
    path('api/login/', login, name='Login'),
    path('api/', include('music_re.api')),
    path('admin/', admin.site.urls),
]
