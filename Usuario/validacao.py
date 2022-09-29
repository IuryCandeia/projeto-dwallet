
from Usuario.models import Usuario


def comparando_senhas(s1, s2):
    if s1 == s2:
        return True
    return False


def duplicidade_email(email):
    colaborador = Usuario.objects.all()

    for colab in colaborador:
        if colab.email == email:
            return True

    return False