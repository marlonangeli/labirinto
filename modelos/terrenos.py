from utils.constantes.mapa import SOLIDO, ROCHOSO, ARENOSO, PANTANO, PAREDE, INICIO, DESTINO, RECOMPENSA


class Terreno:
    def __init__(self, nome, custo):
        self.nome = nome
        self.custo = custo

    @staticmethod
    def cast(terreno: str):
        match = {
            INICIO: SolidoPlano,
            DESTINO: SolidoPlano,
            SOLIDO: SolidoPlano,
            RECOMPENSA: SolidoPlano,
            ROCHOSO: Rochoso,
            ARENOSO: Arenoso,
            PANTANO: Pantano,
            PAREDE: Parede
        }
        return match[terreno]()

    def __str__(self):
        return self.nome[0]


class SolidoPlano(Terreno):
    def __init__(self):
        super().__init__('Solido e plano', 1)


class Rochoso(Terreno):
    def __init__(self):
        super().__init__('Rochoso', 10)


class Arenoso(Terreno):
    def __init__(self):
        super().__init__('Arenoso', 4)


class Pantano(Terreno):
    def __init__(self):
        super().__init__('Pântano', 20)


class Parede(Terreno):
    def __init__(self):
        super().__init__('Parede', float('inf'))
