import pygame
from utils.constantes.cores import *
from utils.constantes.dimensoes import *

screen = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Labirinto IA")

from graficos.texturas import TEXTURAS
from modelos.agente import Agente


def view_map(mapa_, agente=None):
    largura_celula = 32
    altura_celula = 32

    # Desenha cada célula/tile
    for y, linha in enumerate(mapa_):
        for x, celula in enumerate(linha):
            screen.blit(TEXTURAS[celula], (x * largura_celula, y * altura_celula))

    # Desenha o agente
    if agente:
        agente.desenhar(screen)


def draw_button(text, x, y, w, h, color, hover_color=None):
    mx, my = pygame.mouse.get_pos()
    if hover_color and x <= mx <= x + w and y <= my <= y + h:
        pygame.draw.rect(screen, hover_color, (x, y, w, h))
        pygame.draw.rect(screen, color, (x + 4, y + 4, w - 8, h - 8))
    else:
        pygame.draw.rect(screen, color, (x, y, w, h))

    font = pygame.font.SysFont("consolas", 28)
    text_surf = font.render(text, True, WHITE)
    screen.blit(text_surf, (x + w // 2 - text_surf.get_width() // 2, y + h // 2 - text_surf.get_height() // 2))


def game_logic(search_method, map_size):
    print(f"Iniciando jogo com o método {search_method} e tamanho de mapa {map_size}")
    # Aqui, você implementaria a lógica do jogo, usando o método de busca escolhido
    pass


def game_menu(mapa_):
    running = True
    search_methods = ['LARGURA', 'Profundidade', 'Gulosa', 'A*']
    map_sizes = ['Pequeno', 'Médio', 'Grande']

    selected_method = search_methods[0]
    selected_map_size = map_sizes[0]
    agente = Agente(2, 2)

    while running:
        view_map(mapa_)  # Adicionando o mapa como fundo

        agente.mover_aleatoriamente(mapa_)
        agente.desenhar(screen)

        draw_button("Método: " + selected_method, LARGURA // 4, ALTURA // 4, 300, 60, DARKGREEN, GREEN)
        draw_button("Mapa: " + selected_map_size, LARGURA // 4, ALTURA // 4 + 70, 300, 60, DARKGREEN, GREEN)
        draw_button("Iniciar", LARGURA // 4, ALTURA // 2 + 100, 300, 60, DARKRED, RED)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()

                # Método de Busca
                if LARGURA // 4 <= mx <= LARGURA // 4 + 300 and ALTURA // 4 <= my <= ALTURA // 4 + 60:
                    method_index = search_methods.index(selected_method)
                    selected_method = search_methods[(method_index + 1) % len(search_methods)]
                # Tamanho do Mapa
                elif LARGURA // 4 <= mx <= LARGURA // 4 + 300 and ALTURA // 4 + 70 <= my <= ALTURA // 4 + 130:
                    size_index = map_sizes.index(selected_map_size)
                    selected_map_size = map_sizes[(size_index + 1) % len(map_sizes)]
                # Começar o jogo
                elif LARGURA // 4 <= mx <= LARGURA // 4 + 300 and ALTURA // 2 + 100 <= my <= ALTURA // 2 + 160:
                    game_logic(selected_method, selected_map_size)
                    running = False

        pygame.display.flip()
