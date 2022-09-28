from re import template
from django.urls import path
from .views import CadastroView, LoginView
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('cadastro/', CadastroView.as_view(), name='novo_usuario'),
    path('', LoginView.as_view(), name="login_page"),
]
