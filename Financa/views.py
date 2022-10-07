from django.shortcuts import render

from Financa.forms import FinancaForm

def inicio(request):
    return render(request, 'inicio.html')

def add_financa(request):
    context ={}
    context['form']= FinancaForm()
    return render(request, "financa.html", context)