from collections import deque


def busca_em_largura(grafo, inicio, objetivo):
    # Inicialização
    visitados = set()
    fila = deque([inicio])

    inicio.g = 0  # Custo desde o início para o nó inicial é 0

    while fila:
        atual = fila.popleft()

        # Se o nó objetivo for alcançado, retornamos o caminho
        if atual == objetivo:
            caminho = []
            while atual:
                caminho.append(atual)
                atual = atual.pai
            return caminho[::-1]  # Inverte o caminho para ir do início ao fim

        visitados.add(atual)

        for vizinho in grafo.vizinhos(atual):
            if vizinho not in visitados and vizinho not in fila and vizinho.terreno.custo != float('inf'):
                vizinho.pai = atual
                vizinho.g = atual.g + vizinho.custo
                fila.append(vizinho)

    # Se a fila estiver vazia e não encontramos um caminho, retornamos None
    return None
