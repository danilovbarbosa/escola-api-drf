from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula
from escola.validators import validate_cpf


class AlunoSerializer(serializers.ModelSerializer):  # type: ignore
    class Meta:
        model = Aluno
        fields = ["id", "nome", "rg", "cpf", "data_de_nascimento"]

    def validate(self, attrs):
        if not validate_cpf(attrs["cpf"]):
            raise serializers.ValidationError(
                {"cpf": "O CPF deve ter 11 dígitos."}
            )
        return attrs


class CursoSerializer(serializers.ModelSerializer):  # type: ignore
    class Meta:
        model = Curso
        fields = "__all__"


class MatriculaSerializer(serializers.ModelSerializer):  # type: ignore
    class Meta:
        model = Matricula
        fields = "__all__"


class ListaMatriculasAlunoSerializer(serializers.ModelSerializer):  # type: ignore
    curso = serializers.ReadOnlyField(source="curso.descricao")
    periodo = serializers.SerializerMethodField()

    class Meta:
        model = Matricula
        fields = ["curso", "periodo"]

    def get_periodo(self, obj):  # type: ignore
        return obj.get_periodo_display()


class ListaAlunosMatriculadosSerializer(serializers.ModelSerializer):  # type: ignore
    aluno_nome = serializers.ReadOnlyField(source="aluno.nome")

    class Meta:
        model = Matricula
        fields = ["aluno_nome"]
