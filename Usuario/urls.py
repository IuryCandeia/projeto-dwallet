from re import template
from django.urls import path
from Usuario.views import cadastro_form, deletarUsuario, login_view, test
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', login_view, name="login"),
    path('cadastro/', cadastro_form, name="cadastro_form"),
    path('deletar/<id>', deletarUsuario, name='deletar_usuario'),
    path('test', test, name='test'),
    
]
