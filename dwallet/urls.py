
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Usuario.urls'), name='usuario'),
    path('financa/', include('Financa.urls'), name='financa'),
    path('users/', include('users.urls'), name='users'),
]
