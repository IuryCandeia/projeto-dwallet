from re import template
from django.urls import path
from Usuario.views import LoginView, deletarUsuario,  login, login_view, cadastro_form
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('cadastro/', CadastroView.as_view(), name='cadastro_form'),
    # path('', LoginView.as_view(), name="login"),
    path('', login_view, name="login"),
    path('cadastro/', cadastro_form, name="cadastro_form"),
    path('deletar/<id>', deletarUsuario, name='deletar_usuario'),
    
]
