from modelos.terrenos import Terreno
from utils.constantes.mapa import RECOMPENSA, PAREDE


class No:
    def __init__(self, x: int, y: int, terreno: Terreno, recompensa: bool = False):
        self.x = x
        self.y = y
        self.terreno = terreno
        self.recompensa = recompensa

        self.custo = terreno.custo
        self.g = 0  # custo do nó inicial até o nó atual
        self.h = 0  # estimativa do custo do nó atual até o nó objetivo
        self.f = 0  # g + h
        self.pai: No = None
        self.vizinhos: list[No] = []

    @staticmethod
    def criar_no(x: int, y: int, tipo: str) -> 'No':
        if tipo == PAREDE:
            return

        terreno = Terreno.cast(tipo)
        recompensa = False
        if tipo == RECOMPENSA:
            recompensa = True
        return No(x, y, terreno, recompensa)

    def adicionar_pai(self, pai: 'No') -> None:
        if pai == self:
            return
        self.pai = pai
        self.g = pai.g + self.custo
        self.f = self.g + self.h

    def adicionar_vizinho(self, vizinho: 'No') -> None:
        if vizinho == self:
            return
        self.vizinhos.append(vizinho)

    def adicionar_vizinhos(self, vizinhos: list['No']) -> None:
        if self in vizinhos:
            return
        self.vizinhos.extend(vizinhos)

    def __str__(self):
        return f'({self.x},{self.y})'

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash(str(self))

    def __lt__(self, other):
        return self.f < other.f

    def __gt__(self, other):
        return self.f > other.f

    def __le__(self, other):
        return self.f <= other.f

    def __ge__(self, other):
        return self.f >= other.f

    def __ne__(self, other):
        return self.f != other.f
