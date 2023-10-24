from json import dumps, loads


def exportar_json(nome_arquivo, dados):
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(dumps(dados))


def importar_json(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        return loads(arquivo.read())
