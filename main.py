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
    # game_menu()
    agente = Agente(0, 0)
    mapa_gerado = gerar_mapa(25, 25)
    # mapa_gerado = importar_json('mapa.json')
    mapa_para_grafo(mapa_gerado)
    visualizar_mapa(mapa_gerado, agente)

    exportar_json('mapa.json', mapa_gerado)


if __name__ == '__main__':
    main()
