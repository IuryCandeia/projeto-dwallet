
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Usuario.urls'), name='usuario'),
    path('financa/', include('Financa.urls'), name='financa'),
    path('users/', include('users.urls'), name='users'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
