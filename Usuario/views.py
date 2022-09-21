from django.views.generic import TemplateView

class homeView(TemplateView):
    template_name: "main.html"

class cadastroView(TemplateView):
    template_name: "cadastro.html"

class homePageView(TemplateView):
    template_name: "homePage.html"


# def home(request):
#     return render(request, 'home.html')

# def cadastro(request):
#     return render(request, 'cadastro.html')

# def store(request):
#     data = {}
#     if(request.POST['senha'] != request.POST['senha-conf']):
#         data['msg'] = 'Senha e confirmação de senhas diferentes!'
#         data['class'] = 'alert-danger'
#     return render(request, 'cadastro.html', data)