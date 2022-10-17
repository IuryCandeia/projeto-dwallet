from re import template
from django.urls import path
from Usuario.views import cadastro_form, deletarUsuario, login_view, test
from django.conf import settings
from django.conf.urls.static import static

from users.views import home_page, login_request, logout_request, register_request



urlpatterns = [
    path('register', register_request, name='register'),
    path('', home_page, name='home'),
    path('login/', login_request, name='login'),
    path('logout/', logout_request, name='logout'),

]
