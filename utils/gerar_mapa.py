import random

def gerar_mapa(largura, altura, prob_parede=0.3, prob_recompensa=0.03):
    """
    Gera um mapa aleatório.

    :param largura: Largura do mapa.
    :param altura: Altura do mapa.
    :param prob_parede: Probabilidade de uma célula ser uma parede.
    :param prob_recompensa: Probabilidade de uma célula ser uma recompensa.
    :return: Uma lista de listas representando o mapa.
    """
    mapa_ = []

    for _ in range(altura):
        linha = []
        for _ in range(largura):
            r = random.random()  # Gera um número entre 0 e 1

            if r < prob_parede:
                linha.append('▓')
            elif r < prob_parede + prob_recompensa:
                linha.append('$')
            else:
                # Escolhe um terreno aleatoriamente, excluindo parede e recompensa
                terreno = random.choice([' ', 'R', 'A', 'P'])
                linha.append(terreno)

        mapa_.append("".join(linha))
    return mapa_

def mapa_para_grafo(mapa_):
    grafo = {}

    altura = len(mapa_)
    largura = len(mapa_[0]) if mapa_ else 0

    for y in range(altura):
        for x in range(largura):
            if mapa_[y][x] != '▓':  # Se não for uma parede
                vizinhos = []

                # Vizinho de cima
                if y - 1 >= 0 and mapa_[y-1][x] != '▓':
                    vizinhos.append((x, y-1))
                # Vizinho da direita
                if x + 1 < largura and mapa_[y][x+1] != '▓':
                    vizinhos.append((x+1, y))
                # Vizinho de baixo
                if y + 1 < altura and mapa_[y+1][x] != '▓':
                    vizinhos.append((x, y+1))
                # Vizinho da esquerda
                if x - 1 >= 0 and mapa_[y][x-1] != '▓':
                    vizinhos.append((x-1, y))

                grafo[(x, y)] = vizinhos
    print(grafo)
    return grafo