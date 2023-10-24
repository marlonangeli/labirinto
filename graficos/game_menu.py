import pygame
from utils.constantes.cores import *
from utils.constantes.dimensoes import *

screen = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Labirinto IA")

# Desenha botões
def draw_button(text, x, y, w, h, color):
    pygame.draw.rect(screen, color, (x, y, w, h))
    font = pygame.font.SysFont(None, 36)
    text_surf = font.render(text, True, WHITE)
    screen.blit(text_surf, (x + w//2 - text_surf.get_width()//2, y + h//2 - text_surf.get_height()//2))

def game_logic(search_method, map_size):
    print(f"Iniciando jogo com o método {search_method} e tamanho de mapa {map_size}")
    # Aqui, você implementaria a lógica do jogo, usando o método de busca escolhido
    pass

def game_menu():
    running = True
    search_methods = ['Largura', 'Profundidade', 'Gulosa', 'A*']
    map_sizes = ['Pequeno', 'Médio', 'Grande']

    selected_method = search_methods[0]
    selected_map_size = map_sizes[0]

    while running:
        screen.fill(BLUE)

        draw_button("Escolher Método: " + selected_method, largura//4, altura//4, 300, 60, GREEN)
        draw_button("Tamanho do Mapa: " + selected_map_size, largura//4, altura//4 + 70, 300, 60, GREEN)
        draw_button("Iniciar", largura//4, altura//2 + 100, 300, 60, RED)

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