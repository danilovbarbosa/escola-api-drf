from django.db import models


# Create your models here.
class Aluno(models.Model):
    nome = models.CharField(max_length=50)
    rg = models.CharField(max_length=11)
    cpf = models.CharField(max_length=11, unique=True)
    data_de_nascimento = models.DateField()

    def __str__(self) -> str:
        return str(self.nome)


class Curso(models.Model):
    NIVEL = (
        ("B", "Básico"),
        ("I", "Intermediário"),
        ("A", "Avançado"),
    )

    codigo_curso = models.CharField(max_length=50)
    descricao = models.CharField(max_length=11)
    nivel = models.CharField(
        max_length=1, choices=NIVEL, blank=False, null=False, default="B"
    )

    def __str__(self) -> str:
        return str(self.descricao)


class Matricula(models.Model):
    PERIODO = (
        ("M", "Matutino"),
        ("V", "Vespertino"),
        ("N", "Noturno"),
    )

    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    periodo = models.CharField(
        max_length=1, choices=PERIODO, blank=False, null=False, default="M"
    )

    def __str__(self) -> str:
        return str(f"{self.aluno} - {self.curso}")
