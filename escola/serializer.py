from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula


class AlunoSerializer(serializers.ModelSerializer):  # type: ignore
    class Meta:
        model = Aluno
        fields = ["id", "nome", "rg", "cpf", "data_de_nascimento"]

    def validate_cpf(self, cpf: str) -> str:
        if len(cpf) != 11:
            raise serializers.ValidationError("O CPF deve ter 11 dígitos.")
        return cpf

    def validate_nome(self, nome: str) -> str:
        if not nome.isalpha():
            raise serializers.ValidationError(
                "Não inclua números neste campo."
            )
        return nome

    def validate_rg(self, rg: str) -> str:
        if len(rg) != 9:
            raise serializers.ValidationError("O RG deve ter 9 dígitos.")
        return rg

    def validate_celular(self, celular: str) -> str:
        if len(celular) < 11:
            raise serializers.ValidationError("O Celular deve ter 11 dígitos.")
        return celular


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
