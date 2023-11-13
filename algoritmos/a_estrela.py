import copy
import heapq
import time

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
        self.__recompensas_coletadas_array = []
        # propriedades do último caminho encontrado
        self.__custo_total: int = 0
        self.__recompensas_coletadas: int = 0
        self.__recompensas_totais: int = 0
        self.__nos_expandidos: int = 0
        self.__nos_visitados: int = 0
        self.__tempo_execucao: int = 0
        self.__memoria: int = 0

    @property
    def dados_ultima_execucao(self) -> dict:
        return {
            'custo_total': self.__custo_total,
            'recompensas_coletadas': self.__recompensas_coletadas_array,
            'recompensas_totais': self.__recompensas_totais,
            'nos_expandidos': self.__nos_expandidos,
            'nos_visitados': self.__nos_visitados,
            'tempo_execucao': self.__tempo_execucao,
            'memoria': self.__memoria
        }

    def encontrar_caminho(self, debug=False) -> list[list[No]] | None:
        heapq.heappush(self.__abertos, (0, self.inicio))
        custo_total = 0
        custo = 0
        ultima_recompensa = None

        # propriedades
        self.__recompensas_totais = len(self.grafo.recompensas)

        tempo_inicial = time.time()
        while self.__abertos:
            atual: No
            _, atual = heapq.heappop(self.__abertos)

            self.__visitados.append(atual)

            if atual.recompensa and atual not in self.__recompensas_coletadas_array:
                caminho_para_recompensa = []
                if debug:
                    print('-' * 30)

                contador_de_repeticao = 0
                while atual:
                    if debug:
                        print(atual)
                    caminho_para_recompensa.insert(0, atual)
                    atual = atual.pai
                    contador_de_repeticao += 1
                    if contador_de_repeticao > 5000:
                        print('deu pau')
                        return None

                self.__caminho.append(caminho_para_recompensa)
                ultima_recompensa = caminho_para_recompensa[-1]
                self.__recompensas_coletadas_array.append(ultima_recompensa)

                # reseta o grafo e continua a busca
                self.grafo = copy.deepcopy(self.__grafo_original)

                # atualiza o inicio para a ultima recompensa coletada
                atual = self.grafo.encontrar(ultima_recompensa)
                atual.pai = None

                # remove as recompensas coletadas do grafo
                for recompensa in self.__recompensas_coletadas_array:
                    r = self.grafo.encontrar(recompensa)
                    r.recompensa = False
                    r.custo = r.terreno.custo

                # faz uma cópia dos nós abertos para não perder a referência
                abertos = copy.deepcopy(self.__abertos)
                self.__abertos = abertos

                heapq.heappush(self.__abertos, (0, atual))
                custo_total += custo
                custo = 0

            # Se o nó atual for o destino, termina o caminho
            if atual == self.destino:
                caminho_para_destino = []
                if debug:
                    print('-' * 30)
                while atual and atual != ultima_recompensa:
                    if debug:
                        print(atual)
                    # cria uma lista com o caminho percorrido entre as recompensas e o destino
                    caminho_para_destino.insert(0, atual)
                    atual = atual.pai

                self.__recompensas_coletadas = len(self.__recompensas_coletadas_array)
                self.__caminho.append(caminho_para_destino)
                if debug:
                    print('-' * 30)
                    print('Caminho encontrado')
                    print(f'Custo: {custo_total}')
                    print(f'Recompensas coletadas: {self.__recompensas_coletadas}/{self.__recompensas_totais}')

                tempo_final = time.time()
                self.__tempo_execucao = tempo_final - tempo_inicial
                self.__custo_total = custo_total
                self.__recompensas_coletadas_array = len(self.__recompensas_coletadas_array)
                self.__nos_visitados = len(self.__visitados)
                self.__memoria = len(self.__visitados) + len(self.__abertos)

                return self.__caminho

            try:
                for vizinho in self.grafo.nos[atual]:
                    if vizinho in self.__visitados and not vizinho.recompensa:
                        continue

                    atual.g = atual.custo + custo
                    vizinho.pai = atual

                    # se o vizinho for uma recompensa e ainda não foi coletada, o custo é 0
                    if vizinho.recompensa and vizinho not in self.__recompensas_coletadas_array:
                        vizinho.h = 0
                    else:
                        vizinho.g = atual.g + vizinho.custo
                        vizinho.h = self.__calcula_heuristica(vizinho)

                    heapq.heappush(self.__abertos, (vizinho.f, vizinho))
                    self.__nos_expandidos += 1

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
