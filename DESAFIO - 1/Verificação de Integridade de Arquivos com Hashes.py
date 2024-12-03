def verificar_hashes(lista_hashes):
    """
    Verifica a integridade de arquivos comparando o hash fornecido pelo usuário com o hash real do arquivo.

    Entrada:
        Uma lista de pares de hashes (hash calculado e hash esperado), separados por vírgulas, e cada par separado por ponto e vírgula.
        Exemplo: "abc123, abc123; def456, def789"

    Saída:
        Para cada par de hashes fornecido, o código imprime o resultado "Correto" ou "Inválido".
    """
    for hash_comparacao in lista_hashes:
        hash_calculado, hash_esperado = hash_comparacao.split(",")

        # Remove espaços em branco extras que podem ter sido inseridos pelo usuário
        hash_calculado = hash_calculado.strip()
        hash_esperado = hash_esperado.strip()

        if hash_calculado == hash_esperado:
            print("Correto")
        else:
            print("Inválido")

hashes_usuario = input()
lista_hashes = hashes_usuario.split(";")

verificar_hashes(lista_hashes)