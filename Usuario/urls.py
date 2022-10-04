from re import template
from django.urls import path
from Usuario.views import cadastro, cadastroForm, login, inicio, UsuarioCreate
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('cadastro/', CadastroView.as_view(), name='cadastro_form'),
    path('inicio', inicio, name='inicio'),
    path('login', auth_views.LoginView.as_view(
        template_name='form.html'), name="login"),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('cadastro', cadastro, name='cadastro_form'),
    path('modelform', cadastroForm, name="formModel"),
    path('registrar', UsuarioCreate.as_view(), name='registrar'),
]
