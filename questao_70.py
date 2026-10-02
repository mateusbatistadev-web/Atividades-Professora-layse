def buscar_permissao(perfil, indice):
    try:
        return perfil["permissoes"][indice]

    except (KeyError, IndexError):
        return "acesso_restrito"

perfil = {
    "nome": "Administrador",
    "permissoes": ["ler", "editar", "excluir"]
}

indice = int(input("Digite o índice da permissão: "))

print(buscar_permissao(perfil, indice))
