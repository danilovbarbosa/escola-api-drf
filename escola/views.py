from django.db.models.query import QuerySet
from rest_framework import generics, viewsets
from escola.models import Aluno, Curso, Matricula
from escola.serializer import (
    AlunoSerializer,
    CursoSerializer,
    MatriculaSerializer,
    ListaMatriculasAlunoSerializer,
    ListaAlunosMatriculadosSerializer,
)
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class AlunoViewSet(viewsets.ModelViewSet):  # type: ignore
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CursoViewSet(viewsets.ModelViewSet):  # type: ignore
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class MatriculaViewSet(viewsets.ModelViewSet):  # type: ignore
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer


class ListaMatriculasAluno(generics.ListAPIView):  # type: ignore
    """
    Listando as matrículas de um aluno ou aluna
    """

    def get_queryset(self) -> QuerySet:
        queryset = Matricula.objects.filter(aluno_id=self.kwargs["pk"])
        return queryset

    serializer_class = ListaMatriculasAlunoSerializer


class ListaAlunosMatriculados(generics.ListAPIView):  # type: ignore
    """
    Listando alunos e alunas matriculados em um curso
    """

    def get_queryset(self) -> QuerySet:
        queryset = Matricula.objects.filter(curso_id=self.kwargs["pk"])
        return queryset

    serializer_class = ListaAlunosMatriculadosSerializer
