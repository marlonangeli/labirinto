import copy
import heapq
from modelos.grafo import Grafo, No


class AEstrela:
    def __init__(self, grafo: Grafo):
        self.__grafo_original = grafo
        self.grafo = copy.deepcopy(self.__grafo_original)
        self.inicio = self.grafo.inicio
        self.destino = self.grafo.destino
        self.__abertos = []
        self.__visitados = []
        self.__caminho = []
        self.__recompensas_coletadas = []

    def encontrar_caminho(self) -> list[list[No]] | None:
        heapq.heappush(self.__abertos, (0, self.inicio))
        custo = 0
        ultima_recompensa = None

        while self.__abertos:
            atual: No
            _, atual = heapq.heappop(self.__abertos)

            self.__visitados.append(atual)

            if atual.recompensa and atual not in self.__recompensas_coletadas:
                caminho_para_recompensa = []
                print('-' * 30)

                contador_de_repeticao = 0
                while atual:
                    print(atual)
                    caminho_para_recompensa.insert(0, atual)
                    atual = atual.pai
                    contador_de_repeticao += 1
                    if contador_de_repeticao > 10000:
                        print('deu pau')
                        return None

                self.__caminho.append(caminho_para_recompensa)
                ultima_recompensa = caminho_para_recompensa[-1]
                self.__recompensas_coletadas.append(ultima_recompensa)

                # reseta o grafo e continua a busca
                self.grafo = copy.deepcopy(self.__grafo_original)

                # atualiza o inicio para a ultima recompensa coletada
                atual = self.grafo.encontrar(ultima_recompensa)
                atual.pai = None

                # remove as recompensas coletadas do grafo
                for recompensa in self.__recompensas_coletadas:
                    r = self.grafo.encontrar(recompensa)
                    r.recompensa = False
                    r.custo = r.terreno.custo

                self.__abertos = []
                self.__visitados = []
                self.__visitados.append(atual)
                heapq.heappush(self.__abertos, (0, atual))
                custo = 0

            # Se o nó atual for o destino, termina o caminho
            if atual == self.destino:
                caminho_para_destino = []
                print('-' * 30)
                while atual and atual != ultima_recompensa:
                    print(atual)
                    # cria uma lista com o caminho percorrido entre as recompensas e o destino
                    caminho_para_destino.insert(0, atual)
                    atual = atual.pai

                self.__caminho.append(caminho_para_destino)
                print(f'Custo: {custo}')
                return self.__caminho

            try:
                for vizinho in self.grafo.nos[atual]:
                    if vizinho in self.__visitados and not vizinho.recompensa:
                        continue

                    atual.g = atual.custo + custo
                    vizinho.pai = atual

                    # se o vizinho for uma recompensa e ainda não foi coletada, o custo é 0
                    if vizinho.recompensa and vizinho not in self.__recompensas_coletadas:
                        vizinho.h = 0
                    else:
                        vizinho.g = atual.g + vizinho.custo
                        vizinho.h = self.__calcula_heuristica(vizinho)

                    heapq.heappush(self.__abertos, (vizinho.f, vizinho))

                custo += atual.f

            except Exception as e:
                print('Erro ao encontrar caminho', e)

        return None

    def __calcula_heuristica(self, atual: No) -> int:
        # heuristica que busca primeiro todas as recompensas e depois o destino
        recompensas = self.grafo.recompensas

        if not recompensas:
            return distancia_manhattan(atual, self.destino)

        # calcula a recompensa mais proxima com base na posicao atual e o destino final
        recompensa_mais_proxima = min(recompensas, key=lambda recompensa: distancia_manhattan(atual, recompensa))

        # calcula a distancia manhattan entre a recompensa mais proxima e o destino final
        distancia_recompensa_destino = distancia_manhattan(recompensa_mais_proxima, self.destino)

        # calcula a distancia manhattan entre a posicao atual e a recompensa mais proxima
        distancia_atual_recompensa = distancia_manhattan(atual, recompensa_mais_proxima)

        # retorna a soma das duas distancias
        return distancia_recompensa_destino + distancia_atual_recompensa


def distancia_manhattan(no1: No, no2: No) -> int:
    return abs(no1.x - no2.x) + abs(no1.y - no2.y)