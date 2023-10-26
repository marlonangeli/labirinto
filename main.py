import pygame

from algoritmos.a_estrela import a_estrela
from modelos.grafo import Grafo
from utils.constantes.dimensoes import LARGURA, ALTURA

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Labirinto IA")

from graficos.game_menu import game_menu
from modelos.agente import Agente
from graficos.visualizar_mapa import visualizar_mapa, desenhar_caminho
from utils.gerar_mapa import gerar_mapa, mapa_para_grafo
from utils.exportar_arquivo import exportar_json, importar_json


def main():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    agente = Agente(1, 1)
    # mapa_gerado = gerar_mapa(13, 13)
    mapa_gerado = importar_json('mapa.json')
    # exportar_json('mapa.json', mapa_gerado)

    # game_menu(mapa_gerado)

    # visualizar_mapa(mapa_gerado, agente)
    grafo = Grafo(mapa_gerado)
    # visualizar_mapa(mapa_gerado, agente)
    caminho = a_estrela(grafo, grafo.inicio, grafo.destino)
    visualizar_mapa(mapa_gerado, agente, caminho)


if __name__ == '__main__':
    main()
