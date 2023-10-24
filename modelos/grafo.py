class Grafo:
    def __init__(self, mapa_, terrenos, recompensa):
        self.mapa = mapa_
        self.largura = len(mapa_[0])
        self.altura = len(mapa_)
        self.nos = [[None for _ in range(self.largura)] for _ in range(self.altura)]
        self.TERRENOS = terrenos
        self.RECOMPENSA = recompensa

        for y in range(self.altura):
            for x in range(self.largura):
                recompensa = mapa_[y][x] == self.RECOMPENSA
                terreno = self.TERRENOS[' '] if recompensa else self.TERRENOS[mapa_[y][x]]
                self.nos[y][x] = No(x, y, terreno, recompensa)
    def vizinhos(self, no):
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        result = []
        for dir in dirs:
            x, y = no.x + dir[0], no.y + dir[1]
            if 0 <= x < self.largura and 0 <= y < self.altura:
                result.append(self.nos[y][x])
        return result

class No:
    def __init__(self, x, y, terreno, recompensa=False):
        self.x = x
        self.y = y
        self.terreno = terreno
        self.recompensa = recompensa
        self.custo = terreno.custo
        self.pai = None
        self.g = float('inf')  # Custo desde o início
        self.h = 0  # Heurística
        self.f = 0  # f = g + h

    def __str__(self):
        if self.recompensa:
            return self.recompensa
        return str(self.terreno)

