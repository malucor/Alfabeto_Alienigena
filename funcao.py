def ordem_alienigena(palavras):
    grafo = defaultdict(set)
    grau_entrada = defaultdict(int)

    for palavra in palavras:
        for letra in palavra:
            grau_entrada[letra] = 0

    for i in range(1, len(palavras)):
        palavra_ant = palavras[i - 1]
        palavra_atual = palavras[i]
        for j in range(min(len(palavra_ant), len(palavra_atual))):
            if palavra_ant[j] != palavra_atual[j]:
                if palavra_atual[j] not in grafo[palavra_ant[j]]:
                    grafo[palavra_ant[j]].add(palavra_atual[j])
                    grau_entrada[palavra_atual[j]] += 1
                break
        else:
            if len(palavra_ant) > len(palavra_atual):
                return ""

    fila = deque(letra for letra in grau_entrada if grau_entrada[letra] == 0)
    resultado = []
    while fila:
        letra = fila.popleft()
        resultado.append(letra)
        for vizinho in grafo[letra]:
            grau_entrada[vizinho] -= 1
            if grau_entrada[vizinho] == 0:
                fila.append(vizinho)

    if len(resultado) != len(grau_entrada):
        return ""

    return ''.join(resultado)