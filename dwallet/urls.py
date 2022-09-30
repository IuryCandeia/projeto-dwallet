
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuario/', include('Usuario.urls'), name='usuario'),
    path('', include('user.urls'), name='user'),
]
