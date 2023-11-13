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
from graficos.game_menu import game_menu

def main():
    pygame.init()
    pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Labirinto IA")

    mapa_menu = gerar_mapa(21, 21, prob_recompensa=0.05)
    selected_method, selected_map_size = game_menu(mapa_menu)

    if selected_method is None or selected_map_size is None:
        return 

    mapa_gerado = None
    if selected_map_size == 'Pequeno':
        mapa_gerado = gerar_mapa(11, 11, prob_recompensa=0.05)
    elif selected_map_size == 'Médio':
        mapa_gerado = gerar_mapa(17, 17, prob_recompensa=0.05)
    elif selected_map_size == 'Grande':
        mapa_gerado = gerar_mapa(21, 21, prob_recompensa=0.05)
    else:
        mapa_gerado = gerar_mapa(11, 11, prob_recompensa=0.05)

    exportar_json('mapa2.json', mapa_gerado)
    grafo = Grafo(mapa_gerado)
    a_estrela = AEstrela(grafo)
    caminho = a_estrela.encontrar_caminho()
    agente = Agente(grafo.inicio.x, grafo.inicio.y)
    if caminho is None:
        print('Não foi possível encontrar um caminho')
    else:
        visualizar_mapa(mapa_gerado, agente, caminho, selected_method, selected_map_size)

if __name__ == '__main__':
    main()
