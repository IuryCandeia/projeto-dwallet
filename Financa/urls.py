from django.urls import path

from Financa.views import add_financa, inicio

urlpatterns = [
    path('', inicio, name='financa'),
    path('add', add_financa, name='add_financa'),
]
