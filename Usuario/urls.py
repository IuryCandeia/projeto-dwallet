from re import template
from django.urls import path
from Usuario.views import cadastro_form, deletarUsuario, login_view
from Usuario.views import  login
from django.conf import settings
from django.conf.urls.static import static

from users.views import login_request, register_request



urlpatterns = [
    path('', login_request, name="login"),
    path('cadastro/', register_request, name="cadastro_form"),
    path('deletar/<id>', deletarUsuario, name='deletar_usuario'),

]
