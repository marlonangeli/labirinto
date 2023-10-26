import heapq

from modelos.grafo import Grafo, No


def a_estrela(grafo: Grafo, inicio: No, objetivo: No):
    abertos = []
    inicio = grafo.nos[str(inicio)]['no_atual']
    objetivo = grafo.nos[str(objetivo)]['no_atual']

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

        visitados.append(atual)

        try:
            for vizinho in grafo.nos[str(atual)]['vizinhos']:
                if vizinho in visitados:
                    continue

                if vizinho.recompensa:
                    vizinho.custo = 0
                    vizinho.h = 0
                    vizinho.f = vizinho.g + vizinho.h
                    vizinho.pai = atual
                    heapq.heappush(abertos, (vizinho.f, vizinho))
                    continue

                atual.g = atual.custo + custo
                vizinho.g = atual.g + vizinho.custo
                vizinho.h = calcula_heuristica(vizinho, objetivo)
                vizinho.f = vizinho.g + vizinho.h
                vizinho.pai = atual
                heapq.heappush(abertos, (vizinho.f, vizinho))

            custo += atual.f

        except Exception as e:
            print('deu pau mlk')

    return None


def calcula_heuristica(atual, objetivo):
    return abs(objetivo.x - atual.x) + abs(objetivo.y - atual.y)
