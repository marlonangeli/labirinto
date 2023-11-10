import heapq
from modelos.grafo import Grafo, No


class AEstrela:
    def __init__(self, grafo: Grafo):
        self.grafo = grafo
        self.inicio = self.grafo.inicio
        self.destino = self.grafo.destino
        self.__abertos = []
        self.__visitados = []
        self.__caminho = []
        self.__recompensas_coletadas = []

    def encontrar_caminho(self) -> list[No] | None:
        heapq.heappush(self.__abertos, (0, self.inicio))
        custo = 0
        ultima_recompensa = None
        while self.__abertos:
            atual: No
            _, atual = heapq.heappop(self.__abertos)

            if atual.recompensa and atual not in self.__recompensas_coletadas:
                caminho_para_recompensa = []

                while atual.pai:
                    if ultima_recompensa:
                        self.__caminho[-1].pai = ultima_recompensa

                    caminho_para_recompensa.insert(0, atual)
                    atual = atual.pai

                self.__caminho.extend(caminho_para_recompensa)
                self.__recompensas_coletadas.append(caminho_para_recompensa[-1])
                ultima_recompensa = caminho_para_recompensa[-1]
                # retorna de onde parou para continuar a busca
                atual = ultima_recompensa

            # Se o nó atual for o destino, termina o caminho
            if atual == self.destino:
                caminho_para_destino = []
                while atual and atual != ultima_recompensa:
                    # cria uma lista com o caminho percorrido entre as recompensas e o destino
                    caminho_para_destino.insert(0, atual)
                    atual = atual.pai

                self.__caminho.extend(caminho_para_destino)
                print(f'Custo: {custo}')
                return self.__caminho

            self.__visitados.append(atual)

            try:
                for vizinho in self.grafo.nos[atual]:
                    if vizinho in self.__visitados and not vizinho.recompensa:
                        continue

                    atual.g = atual.custo + custo
                    vizinho.pai = atual

                    # se o vizinho for uma recompensa e ainda não foi coletada, o custo é 0
                    if vizinho.recompensa and vizinho not in self.__recompensas_coletadas:
                        vizinho.h = 0
                        vizinho.f = vizinho.g + vizinho.h
                    else:
                        vizinho.g = atual.g + vizinho.custo
                        vizinho.h = self.__calcula_heuristica(vizinho)
                        vizinho.f = vizinho.g + vizinho.h

                    heapq.heappush(self.__abertos, (vizinho.f, vizinho))

                custo += atual.f

            except Exception as e:
                print('Erro ao encontrar caminho', e)

        return None

    def __calcula_heuristica(self, atual: No) -> int:
        # heuristica que busca primeiro todas as recompensas e depois o destino
        recompensas = self.grafo.recompensas

        # remove as recompensas que já foram coletadas
        recompensas_disponiveis = [recompensa for
                                   recompensa in recompensas
                                   if recompensa not in self.__recompensas_coletadas]

        if recompensas_disponiveis:
            recompensa_mais_proxima = min(recompensas_disponiveis,
                                          key=lambda x: abs(x.x - atual.x) + abs(x.y - atual.y))
            objetivo = recompensa_mais_proxima
        else:
            objetivo = self.destino

        return abs(objetivo.x - atual.x) + abs(objetivo.y - atual.y)
