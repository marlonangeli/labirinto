import copy
import time
import sys

from modelos.grafo import Grafo
from modelos.no import No


class BuscaGulosa:
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
        self.__abertos.append(self.inicio)
        custo_total = 0
        custo = 0
        ultima_recompensa = None

        # TODO - tá dando pau

        # propriedades
        self.__recompensas_totais = len(self.grafo.recompensas)

        tempo_inicial = time.time()
        while self.__abertos:
            atual: No
            atual = self.__abertos.pop(0)

            self.__visitados.append(atual)

            if atual.recompensa and atual not in self.__recompensas_coletadas_array:
                caminho_para_recompensa = []
                if debug:
                    print('-' * 30)

                contador_de_repeticao = 0
                for no in self.__caminho:
                    if no == atual:
                        contador_de_repeticao += 1
                        if contador_de_repeticao == 2:
                            break
                    caminho_para_recompensa.append(no)
                caminho_para_recompensa.append(atual)

                self.__caminho = caminho_para_recompensa
                self.__recompensas_coletadas_array.append(atual)
                self.__recompensas_coletadas += 1
                ultima_recompensa = atual
                custo_total += custo
                custo = 0

                if debug:
                    print(f'Coletada recompensa {atual}')
                    print(f'Custo total: {custo_total}')
                    print(f'Recompensas coletadas: {self.__recompensas_coletadas}/{self.__recompensas_totais}')
                    print(f'Nós expandidos: {self.__nos_expandidos}')
                    print(f'Nós visitados: {self.__nos_visitados}')
                    print(f'Tempo de execução: {self.__tempo_execucao:0.2f} UTR (Unidade de Tempo Rápido)')
                    print(f'Memória: {self.__memoria} QI (Quilobytes de Informação)')
                    print(f'Caminho: {self.__caminho}')
                    print('-' * 30)

                if self.__recompensas_coletadas == self.__recompensas_totais:
                    self.__custo_total = custo_total
                    self.__tempo_execucao = time.time() - tempo_inicial
                    self.__memoria = sys.getsizeof(self)
                    return self.__caminho

                self.__abertos = []
                self.__visitados = []
                self.grafo = copy.deepcopy(self.__grafo_original)
                self.inicio = atual
                self.__abertos.append(atual)
                custo_total = 0
                custo = 0
                continue

            if atual == self.destino:
                self.__caminho.append(atual)
                self.__custo_total = custo_total
                self.__tempo_execucao = time.time() - tempo_inicial
                self.__memoria = sys.getsizeof(self)
                return self.__caminho

            self.__caminho.append(atual)
            custo += atual.custo
            self.__nos_expandidos += 1

            for vizinho in atual.vizinhos:
                if vizinho not in self.__visitados and vizinho not in self.__abertos:
                    vizinho.adicionar_pai(atual)
                    self.__abertos.append(vizinho)
                    self.__nos_visitados += 1

            self.__abertos.sort(key=lambda no: no.h, reverse=True)

        self.__tempo_execucao = time.time() - tempo_inicial
        self.__memoria = sys.getsizeof(self)
        return None

    def __calcula_heuristica(self, no: No) -> int:
        return abs(no.x - self.destino.x) + abs(no.y - self.destino.y)
