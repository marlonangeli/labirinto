import heapq

from modelos.grafo import Grafo, No


def a_estrela(grafo: Grafo, inicio: No, objetivo: No):
    abertos = []

    heapq.heappush(abertos, (0, inicio))
    visitados = []

    custo = 0
    while abertos:
        _, atual = heapq.heappop(abertos)
        if atual == objetivo:
            caminho = []
            while atual.pai:
                caminho.insert(0, atual)
                atual = atual.pai
            caminho.insert(0, atual)
            return caminho

        # visitados.add(atual)
        visitados.append(atual)
        for vizinho in grafo.vizinhos(atual):
            if vizinho in visitados:
                continue
            atual.g = atual.custo + custo
            vizinho.g = atual.g + vizinho.custo
            vizinho.h = calcula_heuristica(vizinho, objetivo)
            vizinho.f = vizinho.g + vizinho.h
            vizinho.pai = atual
            heapq.heappush(abertos, (vizinho.f, vizinho))

        custo += atual.f

    return None


def calcula_heuristica(atual, objetivo):
    return abs(objetivo.x - atual.x) + abs(objetivo.y - atual.y)
