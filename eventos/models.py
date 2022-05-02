from django.db import models

"""
    Classe ``Evento`` define a tabela de eventos no banco de dados
"""
class Eventos(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    localData = models.CharField(max_length=100)
    edicao = models.DateField(auto_now=True)
    
class Nomes(models.Model):
    evento_id = models.ForeignKey(Eventos, on_delete=models.CASCADE)
    nome = models.CharField(max_length=150)