from django import forms 
from .models import ExplorarModel

class ExplorarForm(forms.ModelForm):
    class Meta:
        model = ExplorarModel
        fields = ['titulo','descricao','categoria','completo',]
            