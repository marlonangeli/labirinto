import pygame

from algoritmos.a_estrela import AEstrela
from modelos.grafo import Grafo
from utils.constantes.dimensoes import LARGURA, ALTURA
from utils.exportar_arquivo import exportar_json, importar_json

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Labirinto IA")

from modelos.agente import Agente
from graficos.visualizar_mapa import visualizar_mapa
from utils.gerar_mapa import gerar_mapa


def main():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    mapa_gerado = gerar_mapa(13, 13, prob_recompensa=0.05)
    mapa_gerado = importar_json('mapa1.json')
    # exportar_json('mapa1.json', mapa_gerado)

    # game_menu(mapa_gerado)
    grafo = Grafo(mapa_gerado)
    a_estrela = AEstrela(grafo)
    caminho = a_estrela.encontrar_caminho()
    agente = Agente(grafo.inicio.x, grafo.inicio.y)
    if caminho is None:
        print('Não foi possível encontrar um caminho')
    visualizar_mapa(mapa_gerado, agente, caminho, "Algoritmo A Estrela", "Pequeno")


if __name__ == '__main__':
    main()
