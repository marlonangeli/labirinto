import random
import numpy as np
from utils.constantes.mapa import PAREDE, RECOMPENSA, SOLIDO, ROCHOSO, ARENOSO, PANTANO, DESTINO, INICIO


def gerar_mapa(largura, altura, prob_recompensa=0.03):
    """
    Gera um mapa aleatório.

    :param largura: Largura do mapa.
    :param altura: Altura do mapa.
    :param prob_parede: Probabilidade de uma célula ser uma parede.
    :param prob_recompensa: Probabilidade de uma célula ser uma recompensa.
    :return: Uma lista de listas representando o mapa.
    """
    mapa_ = []
    linhas = altura
    colunas = largura

    labirinto = gerar_labirinto(linhas, colunas)

    for linha in labirinto:
        nova_linha = []
        for cell in linha:
            if cell == 0:  # Parede
                nova_linha.append(PAREDE)
            elif cell == 1:  # Chão
                nova_linha.append('')
            elif cell == 2:  # Destino
                nova_linha.append(DESTINO)
            elif cell == -1:  # Início
                nova_linha.append(INICIO)
            else:
                nova_linha.append('')
        mapa_.append(nova_linha)

    for i in range(1, linhas - 1):
        for j in range(1, colunas - 1):
            if mapa_[i][j] == PAREDE\
                    or mapa_[i][j] == DESTINO\
                    or mapa_[i][j] == INICIO:
                continue
            if random.random() < prob_recompensa:
                mapa_[i][j] = RECOMPENSA
            else:
                # Se não for recompensa, é um dos terrenos
                terreno = random.choice([SOLIDO, ROCHOSO, ARENOSO, PANTANO])
                mapa_[i][j] = terreno

    return mapa_


def gerar_labirinto(linhas, colunas):
    linhas_internas = linhas - 2
    colunas_internas = colunas - 2
    grid_interno = np.zeros((linhas_internas, colunas_internas), dtype=int)

    def is_valid(linhas, colunas):
        return 0 <= linhas < linhas_internas and 0 <= colunas < colunas_internas

    def pegar_colunas_adjacente(linhas, colunas):
        paredes_adjacentes = []
        direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dir_l, dir_c in direcoes:
            nova_lin, nova_col = linhas + dir_l * 2, colunas + dir_c * 2
            if is_valid(nova_lin, nova_col) and grid_interno[nova_lin][nova_col] == 0:
                paredes_adjacentes.append(((linhas + dir_l, colunas + dir_c), (nova_lin, nova_col)))

        return paredes_adjacentes

    nos_visitados = set()
    # Define início e fim do labirinto aleatoriamente no lado esquerdo e direito e marca como visitado
    linha_inicio, coluna_inicio = 0, random.randint(0, colunas_internas - 1)
    linha_destino, coluna_destino = linhas_internas - 1, random.randint(0, colunas_internas - 1)
    grid_interno[linha_inicio][coluna_inicio] = 1
    nos_visitados.add((linha_inicio, coluna_inicio))
    paredes = pegar_colunas_adjacente(linha_inicio, coluna_inicio)

    while paredes:
        (parede_lin, parede_col), (no_lin, no_col) = random.choice(paredes)
        paredes.remove(((parede_lin, parede_col), (no_lin, no_col)))

        if (no_lin, no_col) not in nos_visitados:
            grid_interno[parede_lin][parede_col] = 1
            grid_interno[no_lin][no_col] = 1
            nos_visitados.add((no_lin, no_col))
            paredes.extend(pegar_colunas_adjacente(no_lin, no_col))

    grid_interno[linha_destino][coluna_destino] = 2
    grid_interno[linha_inicio][coluna_inicio] = -1

    grid = np.zeros((linhas, colunas), dtype=int)
    grid[1:-1, 1:-1] = grid_interno

    return grid


def mapa_para_grafo(mapa_):
    grafo = {}

    altura = len(mapa_)
    largura = len(mapa_[0]) if mapa_ else 0

    for y in range(altura):
        for x in range(largura):
            if mapa_[y][x] != PAREDE:  # Se não for uma parede
                vizinhos = []

                # Vizinho de cima
                if y - 1 >= 0 and mapa_[y - 1][x] != PAREDE:
                    vizinhos.append((x, y - 1))
                # Vizinho da direita
                if x + 1 < largura and mapa_[y][x + 1] != PAREDE:
                    vizinhos.append((x + 1, y))
                # Vizinho de baixo
                if y + 1 < altura and mapa_[y + 1][x] != PAREDE:
                    vizinhos.append((x, y + 1))
                # Vizinho da esquerda
                if x - 1 >= 0 and mapa_[y][x - 1] != PAREDE:
                    vizinhos.append((x - 1, y))

                grafo[(x, y)] = vizinhos

    print(grafo)
    return grafo
