import pygame
from utils.constantes.cores import *
from utils.constantes.dimensoes import *
from graficos.texturas import TEXTURAS
from modelos.agente import Agente

screen = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Labirinto IA")

def visualizar_mapa(mapa_, agente=None):
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

    font = pygame.font.SysFont("arial", 28)
    text_surf = font.render(text, True, WHITE)
    screen.blit(text_surf, (x + w // 2 - text_surf.get_width() // 2, y + h // 2 - text_surf.get_height() // 2))


def game_logic(search_method, map_size):
    print(f"Iniciando jogo com o método {search_method} e tamanho de mapa {map_size}")
    # Aqui, você implementaria a lógica do jogo, usando o método de busca escolhido
    pass

def game_menu(mapa_):
    running = True
    search_methods = ['Largura', 'Profundidade', 'Gulosa', 'A*']
    map_sizes = ['Pequeno', 'Médio', 'Grande']

    selected_method = search_methods[0]
    selected_map_size = map_sizes[0]
    agente = Agente(2, 2)

    while running:
        visualizar_mapa(mapa_)  # Adicionando o mapa como fundo

        agente.mover_aleatoriamente(mapa_)
        agente.desenhar(screen)

        draw_button("Método: " + selected_method, largura//4, altura//4, 300, 60, DARKGREEN, GREEN)
        draw_button("Mapa: " + selected_map_size, largura//4, altura//4 + 70, 300, 60, DARKGREEN, GREEN)
        draw_button("Iniciar", largura//4, altura//2 + 100, 300, 60, DARKRED, RED)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                
                # Método de Busca
                if largura//4 <= mx <= largura//4 + 300 and altura//4 <= my <= altura//4 + 60:
                    method_index = search_methods.index(selected_method)
                    selected_method = search_methods[(method_index + 1) % len(search_methods)]
                # Tamanho do Mapa
                elif largura//4 <= mx <= largura//4 + 300 and altura//4 + 70 <= my <= altura//4 + 130:
                    size_index = map_sizes.index(selected_map_size)
                    selected_map_size = map_sizes[(size_index + 1) % len(map_sizes)]
                # Começar o jogo
                elif largura//4 <= mx <= largura//4 + 300 and altura//2 + 100 <= my <= altura//2 + 160:
                    game_logic(selected_method, selected_map_size)
                    running = False

        pygame.display.flip()
