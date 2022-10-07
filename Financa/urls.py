from django.urls import path

from Financa.views import inicio

urlpatterns = [
    path('', inicio, name='financa'),
]
