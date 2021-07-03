def validate_cpf(cpf: str) -> bool:
    return len(cpf) != 11


# def validate_nome(self, nome: str) -> str:
#     if not nome.isalpha():
#         raise serializers.ValidationError(
#             "Não inclua números neste campo."
#         )
#     return nome

# def validate_rg(self, rg: str) -> str:
#     if len(rg) != 9:
#         raise serializers.ValidationError("O RG deve ter 9 dígitos.")
#     return rg

# def validate_celular(self, celular: str) -> str:
#     if len(celular) < 11:
#         raise serializers.ValidationError("O Celular deve ter 11 dígitos.")
#     return celular