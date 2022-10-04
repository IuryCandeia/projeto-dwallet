from django.urls import path
from .views import deletarUser, editar, editarUser, salvar, userHome
urlpatterns = [
    path('', userHome, name='userHome'),
    path('salvar', salvar, name='salvar'),
    path('editar/<int:id>', editar, name='editar'),
    path('update/<int:id>', editarUser, name='update'),
    path('delete/<int:id>', deletarUser, name='deletar'),
    
]
