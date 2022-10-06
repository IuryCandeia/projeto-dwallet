
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Usuario.urls'), name='usuario'),
    path('user/', include('user.urls'), name='user'),
]
