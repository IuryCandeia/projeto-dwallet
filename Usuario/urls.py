from re import template
from django.urls import path
from Usuario.views import LoginView, cadastro, cadastroForm, login
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('cadastro/', CadastroView.as_view(), name='cadastro_form'),
    # path('', LoginView.as_view(), name="login"),
    path('cadastro/', cadastro, name='cadastro_form'),
    path('', login, name="login"),
    path('modelform', cadastroForm, name="form"),
]
