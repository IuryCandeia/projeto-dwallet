from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout

def register_request(request):
	title_error = None
	text_error = None
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("login")
		else:
			title_error = 'EMAIL OU SENHA INCORRETO'
			text_error = 'EMAIL OU SENHA INCORRETO'
			dados = {
				'title_error': title_error,
				'text_error': text_error,
			}

			descricao = f'{title_error} - {text_error}'
			error_sucess = 'error'
			return render(request, 'users/register.html', dados)
	form = NewUserForm()
	return render (request=request, template_name="users/register.html", context={"form":form})

def home_page(request):
    return render(request, 'users/home_page.html')

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		print('ghere')
		print(form)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="users/login_page.html", context={"form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "Logout efetuado com sucesso.") 
	return redirect('login_page')