from utils.constantes.mapa import RECOMPENSA, SOLIDO, DESTINO, INICIO, PAREDE
from modelos.terrenos import Terreno

class Grafo:
    def __init__(self, mapa):
        self.mapa = mapa
        self.largura = len(mapa[0])
        self.altura = len(mapa)
        self.nos, self.inicio, self.destino = self.mapa_para_grafo(mapa)

    @staticmethod
    def mapa_para_grafo(mapa):
        grafo = {}

        altura = len(mapa)
        largura = len(mapa[0]) if mapa else 0

        inicio = None
        destino = None

        for y in range(altura):
            for x in range(largura):
                if mapa[y][x] != PAREDE:  # Se não for uma parede
                    vizinhos = []
                    no = No(x, y, Terreno.cast(mapa[y][x]))
                    if mapa[y][x] == RECOMPENSA:
                        no.recompensa = True

                    if mapa[y][x] == INICIO:
                        inicio = no
                    elif mapa[y][x] == DESTINO:
                        destino = no

                    grafo[str(no)] = {
                        'no_atual': no,
                        'vizinhos': vizinhos
                    }

                    # Vizinho de cima
                    if y - 1 >= 0 and mapa[y - 1][x] != PAREDE:
                        vizinhos.append(No(x, y - 1, Terreno.cast(mapa[y - 1][x])))
                    # Vizinho da direita
                    if x + 1 < largura and mapa[y][x + 1] != PAREDE:
                        vizinhos.append(No(x + 1, y, Terreno.cast(mapa[y][x + 1])))
                    # Vizinho de baixo
                    if y + 1 < altura and mapa[y + 1][x] != PAREDE:
                        vizinhos.append(No(x, y + 1, Terreno.cast(mapa[y + 1][x])))
                    # Vizinho da esquerda
                    if x - 1 >= 0 and mapa[y][x - 1] != PAREDE:
                        vizinhos.append(No(x - 1, y, Terreno.cast(mapa[y][x - 1])))

        return grafo, inicio, destino

    def vizinhos(self, no):
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        result = []
        for direcao in dirs:
            x, y = no.x + direcao[0], no.y + direcao[1]
            if 0 <= x < self.largura and 0 <= y < self.altura and self.mapa[y][x] != PAREDE:
                # Verifica se a chave existe
                if str(No(x, y, Terreno.cast(self.mapa[y][x]))) in self.nos:
                    result.append(self.nos[str(No(x, y, Terreno.cast(self.mapa[y][x])))]['no_atual'])

        return result


class No:
    def __init__(self, x: int, y: int, terreno: Terreno, recompensa: bool = False):
        self.x = x
        self.y = y
        self.terreno = terreno
        self.recompensa = recompensa
        self.custo = terreno.custo
        self.pai : No = None
        self.g = float('inf')  # Custo desde o início
        self.h = 0  # Heurística
        self.f = 0  # f = g + h

    def __str__(self):
        if self.recompensa:
            return 'R' + str(self.x) + str(self.y)
        return str(self.terreno) + str(self.x) + str(self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __lt__(self, other):
        return self.f < other.f

    def __gt__(self, other):
        return self.f > other.f

    def __le__(self, other):
        return self.f <= other.f

    def __ge__(self, other):
        return self.f >= other.f
