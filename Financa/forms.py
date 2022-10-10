from django import forms

from Financa.models import Financa




class FinancaForm(forms.Form):
    titulo = forms.CharField(label= 'Título',widget=forms.TextInput(
        attrs={'placeholder': 'Título', 'class': 'form-group', }), max_length=100, min_length=3, required=True)
    descricao = forms.CharField(label='Descrição' ,widget=forms.Textarea(
        attrs={'placeholder': 'Descrição', 'class': 'form-control', }))
    valor = forms.DecimalField(required=True, max_digits=20, decimal_places=2)

    def save(self):
        data = self.cleaned_data
        f = Financa(titulo=data['titulo'], descricao=data['descricao'], valor=data['valor'])
        f.save()