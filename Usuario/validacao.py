
from Usuario.models import Usuario


def comparando_senhas(s1, s2):
    if s1 == s2:
        return True
    return False


def duplicidade_email(email):
    usuario = Usuario.objects.all()
    for user in usuario:
        if user.email == email:
            return True
    return False


def duplicidade_id(id):
    usuario = Usuario.objects.all()

    for user in usuario:
        if user.username == id:
            return True

    return False


def logado(request):
    if request.user.is_authenticated:
        return True
    else:
        return False