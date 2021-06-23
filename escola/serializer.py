from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula


class AlunoSerializer(serializers.ModelSerializer):  # type: ignore
    class Meta:
        model = Aluno
        fields = ["id", "nome", "rg", "cpf", "data_de_nascimento"]


class CursoSerializer(serializers.ModelSerializer):  # type: ignore
    class Meta:
        model = Curso
        fields = "__all__"


class MatriculaSerializer(serializers.ModelSerializer):  # type: ignore
    class Meta:
        model = Matricula
        fields = "__all__"


class ListaMatriculasAlunoSerializer(serializers.ModelSerializer):  # type: ignore
    class Meta:
        model = Matricula
        fields = ["curso", "periodo"]
