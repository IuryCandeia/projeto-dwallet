from pyexpat.errors import messages
from django.views.generic import TemplateView
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from .models import Usuario

class homeView(TemplateView):
    template_name: "main.html"

class cadastroView(TemplateView):
    template_name: "cadastro.html"

class homePageView(TemplateView):
    template_name: "homePage.html"



def cadastro(request):
    try:
        if request.method == "POST":
        
            email = request.POST["email"]
            nome = request.POST["nome"]
            numero = request.POST['numero']
            senha = request.POST["new-password"]
            senhaConf= request.POST["confirm-new-password"]

            if email.find('@') == -1:
                messages.error(
                    request, "Email no formato errado, insira um email institucional")
                return redirect("cadastro")
            elif (email.find('@') != -1) and email[email.find('@'):] != '@fiponline.edu.br':
                messages.error(
                    request, "Por Favor insira o seu email institucional. ex:nome_sobrenome@fiponline.edu.br")
                return redirect("cadastro")

            if campo_vazio(email):
                messages.error(request, "O campo email não pode ficar em Branco")
                return redirect("cadastro")
            if campo_vazio(nome):
                messages.error(request, "O campo Nome não pode ficar em Branco")
                return redirect("cadastro")
            if campo_vazio(numero):
                messages.error(request, "O campo Tel não pode ficar em Branco")
                return redirect("cadastro")
            if senhas_nao_sao_iguais(senha, senhaConf):
                messages.error(request, 'As senhas não são iguais')
                return redirect("cadastro")
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Usuário já cadastrado ')
                return redirect("cadastro")
            code = ''
            for x in range(6):
                code = code + str(random.randint(0, 9))

            user = Usuario.objects.create_user(email=email, nome=nome, numero=numero, password=senha, status_validado=True, code_validado=code)
            user.save()

            messages.success(request, 'Colaborador cadastrado com sucesso')
            return redirect('login')

            # Cadastro com código 
            # return redirect("corfirmacao_code", user.id)
        else:

            return render(request, "colaborador/cadastro.html")
    except:
        messages.error(request, 'Ops, Tivemos um pequeno problema inesperado.Recarregue a página e logue novamente')
        return redirect('login')


def login(request):
    try:
        if request.method == 'POST':
            email = request.POST['email']
            senha = request.POST['senha']

            if campo_vazio(email) or campo_vazio(senha):
                messages.error(request, 'Campo email e senha não podem ser vazios')
                return redirect('login')
            
            if Usuario.objects.filter(email=email).exists():
                try:            
                    col = get_object_or_404(Colaborador, email=email)
                except:
                    messages.error(request, 'Tivemos um pequeno problema.Recarregue a página e logue novamente')
                    return redirect('login')
                nome = Colaborador.objects.filter(
                    email=email).values_list('username', flat=True).get()

                colaborador = auth.authenticate(
                    request, username=nome, password=senha)

                if colaborador != None:
                    auth.login(request, colaborador)

                    if col.status_validado == False:
                        return redirect("corfirmacao_code", col.id)
                    return redirect('dashboard')
                else:
                    messages.error(request, "Email ou senha não confere")
            else:
                messages.error(request, "Email não cadastrado")
        return render(request, "colaborador/login.html")
    except:
        messages.error(request, 'Ops, Tivemos um pequeno problema inesperado.Recarregue a página e logue novamente')
        return redirect('login')

def senhas_nao_sao_iguais(senha, senha2):
    return senha != senha2
def campo_vazio(campo):
    return not campo.strip()