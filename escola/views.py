from django.db.models.query import QuerySet
from rest_framework import generics, viewsets
from escola.models import Aluno, Curso, Matricula
from escola.serializer import (
    AlunoSerializer,
    CursoSerializer,
    MatriculaSerializer,
    ListaMatriculasAlunoSerializer,
)


class AlunoViewSet(viewsets.ModelViewSet):  # type: ignore
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


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
