from django.urls import path, include
from rest_framework import routers
from escola.views import (
    AlunoViewSet,
    CursoViewSet,
    MatriculaViewSet,
    ListaMatriculasAluno,
    ListaAlunosMatriculados,
)

router = routers.DefaultRouter()
router.register("alunos", AlunoViewSet, basename="Alunos")
router.register("cursos", CursoViewSet, basename="Cursos")
router.register("matriculas", MatriculaViewSet, basename="Matriculas")


urlpatterns = [
    path("", include(router.urls)),
    path("aluno/<int:pk>/matriculas/", ListaMatriculasAluno.as_view()),
    path("curso/<int:pk>/matriculas/", ListaAlunosMatriculados.as_view()),
]
