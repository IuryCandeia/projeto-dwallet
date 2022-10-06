from re import template
from django.urls import path
from Usuario.views import LoginView,  login, user_form
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('cadastro/', CadastroView.as_view(), name='cadastro_form'),
    # path('', LoginView.as_view(), name="login"),
    path('', LoginView.as_view(), name="login"),
    path('form', user_form, name="user_form"),
]
