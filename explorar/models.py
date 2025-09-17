from django.db import models
from datetime import date

# Create your models here.
class ExplorarModel(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    categoria = models.CharField(max_length=50, blank=True, null=True)
    data_criacao = models.DateField(auto_now_add=True)
    completo = models.BooleanField(default=False)
    imagem = models.ImageField(upload_to='explorar_fotos/', null=True, blank=True)

    def __str__(self):
        return self.titulo
    
    