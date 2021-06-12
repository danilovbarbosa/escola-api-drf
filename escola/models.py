from django.db import models


# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=50)
    rg = models.CharField(max_length=11)
    cpf = models.CharField(max_length=11)
    data_de_nascimento = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.nome
