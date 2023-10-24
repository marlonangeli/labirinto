import pygame
from utils.constantes.dimensoes import LARGURA, ALTURA
from graficos.game_menu import game_menu
from modelos.agente import Agente
from graficos.visualizar_mapa import visualizar_mapa
from utils.gerar_mapa import gerar_mapa, mapa_para_grafo
from utils.exportar_arquivo import exportar_json, importar_json


def main():
    pygame.init()
    tela = pygame.display.set_mode((LARGURA, ALTURA))
    agente = Agente(1, 1)
    mapa_gerado = gerar_mapa(20, 20)
    visualizar_mapa(mapa_gerado, agente)
    # mapa_grafo = mapa_para_grafo(mapa_gerado)
    # game_menu(mapa_gerado)

    exportar_json('mapa.json', mapa_gerado)


if __name__ == '__main__':
    main()
