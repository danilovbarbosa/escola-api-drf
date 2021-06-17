from django.contrib import admin
from escola.models import Aluno, Curso, Matricula


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ["id", "nome", "rg", "cpf", "data_de_nascimento"]
    list_display_links = ["id", "nome"]
    search_fields = ["nome"]
    list_per_page = 20


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "codigo_curso",
        "descricao",
        "nivel",
    ]
    list_display_links = ["id", "codigo_curso"]
    search_fields = ["codigo_curso"]
    list_per_page = 20


@admin.register(Matricula)
class MatriculaAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "aluno",
        "curso",
        "periodo",
    ]
    list_display_links = ["id", "aluno", "curso", "periodo"]
