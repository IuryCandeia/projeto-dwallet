from re import template
from django.urls import path
from .views import homeView, cadastroView, homePageView

urlpatterns = [
    path('', homeView.as_view(template_name="login.html"), name='home'),
    path('cadastro/', cadastroView.as_view(template_name="cadastro.html"), name='cadastro'),
    path('homepage/', homePageView.as_view(template_name="homepage.html"), name="homepage")
]
