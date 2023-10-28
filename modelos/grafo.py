from modelos.no import No
from utils.constantes.mapa import INICIO, DESTINO


class Grafo:
    def __init__(self, mapa):
        self.__mapa = mapa
        self.nos: dict[No, list[No]] = {}
        self.__criar_grafo()

    @property
    def inicio(self) -> No:
        x, y = self.__encontrar_no_mapa(INICIO)
        return self.__encontrar_por_coordenada(x, y)

    @property
    def destino(self) -> No:
        x, y = self.__encontrar_no_mapa(DESTINO)
        return self.__encontrar_por_coordenada(x, y)

    @property
    def recompensas(self) -> list[No]:
        recompensas = []
        for no in self.nos:
            if no.recompensa:
                recompensas.append(no)

        return recompensas

    def __criar_grafo(self):
        grafo = {}

        def encontrar_vizinhos(no: No) -> list[No]:
            vizinhos = []
            for x in range(no.x - 1, no.x + 2):
                for y in range(no.y - 1, no.y + 2):
                    if x == no.x and y == no.y:
                        continue

                    vizinho = self.__encontrar_no_mapa(x, y)
                    _no = No.criar_no(x, y, vizinho)

                    if vizinho and _no:
                        _no.adicionar_pai(no)
                        vizinhos.append(_no)

            return vizinhos

        for x, linha in enumerate(self.__mapa):
            for y, coluna in enumerate(linha):
                no = No.criar_no(x, y, coluna)
                if not no:
                    continue
                vizinhos = encontrar_vizinhos(no)
                grafo[no] = vizinhos
                no.adicionar_vizinhos(vizinhos)

        self.nos = grafo

    def __encontrar_no_mapa(self, valor: str) -> tuple[int, int] | tuple[None, None]:
        for x, linha in enumerate(self.__mapa):
            for y, coluna in enumerate(linha):
                if coluna == valor:
                    return x, y

        return None, None

    def __encontrar_no_mapa(self, x: int, y: int) -> str | None:
        no = self.__mapa[x][y]
        if no:
            return no

        return None

    def __encontrar_por_coordenada(self, x: int, y: int) -> No | None:
        for no in self.nos:
            if no.x == x and no.y == y:
                return no

        return None
