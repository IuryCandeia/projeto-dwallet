from django.urls import path
from .views import editar, salvar, userHome

urlpatterns = [
    path('', userHome, name='userHome'),
    path('salvar', salvar, name='salvar'),
    path('editar/<int:id>', editar, name='editar'),
]
