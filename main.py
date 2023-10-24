import pygame
from utils.constantes.dimensoes import LARGURA, ALTURA
from graficos.game_menu import game_menu
from modelos.agente import Agente
from graficos.visualizar_mapa import visualizar_mapa
from utils.gerar_mapa import gerar_mapa, mapa_para_grafo


def main():
    pygame.init()
    tela = pygame.display.set_mode((largura, altura))
    agente = Agente(0, 0)
    mapa_gerado = gerar_mapa(20, 20)
    game_menu(mapa_gerado)


if __name__ == '__main__':
    main()
