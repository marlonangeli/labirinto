class Terreno:
    def __init__(self, nome, custo):
        self.nome = nome
        self.custo = custo

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
