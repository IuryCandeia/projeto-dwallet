from re import template
from django.urls import path
from Usuario.views import  Register, deletarUsuario, login_page, test
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    # path('cadastro/', CadastroView.as_view(), name='cadastro_form'),
    # path('', LoginView.as_view(), name="login"),
    path('', login_page, name="login"),
    path('cadastro/', Register, name="cadastro_form"),
    path('deletar/<id>', deletarUsuario, name='deletar_usuario'),
    path('test', test, name='test'),
    
]
