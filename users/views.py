from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			messages.success(request, "Registration successful." )
			return render(request, "users/home_page.html")
		messages.error(request, "Não foi possível completar o cadastro, informações inválidas.")
	form = NewUserForm()
	return render (request=request, template_name="users/register.html", context={"form":form})

def home_page(request):
    return render(request, 'users/home_page.html')

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		print('ghere')
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"Você está logado como {username}.")
				return redirect("home")
			else:
				messages.error(request,"Username ou senha inválidos.")
		else:
			messages.error(request,"Username ou senha inválidos.")
	form = AuthenticationForm()
	return render(request=request, template_name="users/login_page.html", context={"form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "Logout efetuado com sucesso.") 
	return redirect('login_page')