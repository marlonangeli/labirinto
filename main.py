import pygame
pygame.init()
from utils.constantes.dimensoes import largura, altura
tela = pygame.display.set_mode((largura, altura))
from graficos.game_menu import game_menu
from modelos.agente import Agente
from graficos.visualizar_mapa import visualizar_mapa
from utils.gerar_mapa import gerar_mapa, mapa_para_grafo
agente = Agente(0, 0)  
mapa_gerado = gerar_mapa(20, 20)
game_menu(mapa_gerado)
##mapa_para_grafo(mapa_gerado)
##visualizar_mapa(mapa_gerado, agente)