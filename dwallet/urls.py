
from django.contrib import admin
from django.urls import path
from Usuario.views import home, store, cadastro

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('cadastro/', cadastro),
    path('db/', store),
]
