from django.shortcuts import render

from Financa.forms import FinancaForm

def inicio(request):
    return render(request, 'inicio.html')

def add_financa(request):
    context ={}
    context['form']= FinancaForm()
    form = FinancaForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
    return render(request, "financa.html", context)