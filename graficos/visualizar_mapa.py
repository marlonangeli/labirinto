import pygame
from graficos.texturas import TEXTURAS
def visualizar_mapa(mapa_, agente=None):
    largura_celula = 32
    altura_celula = 32

    largura_tela = len(mapa_[0]) * largura_celula
    altura_tela = len(mapa_) * altura_celula

    tela = pygame.display.set_mode((largura_tela, altura_tela))
    pygame.display.set_caption("Visualização do Mapa")

    rodando = True
    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False

        tela.fill((255, 255, 255)) 

        # Desenha cada célula/tile
        for y, linha in enumerate(mapa_):
            for x, celula in enumerate(linha):
                tela.blit(TEXTURAS[celula], (x * largura_celula, y * altura_celula))

        # Desenha o agente
        if agente:
            agente.desenhar(tela)

        # Aqui, você pode adicionar o código para mostrar os botões e opções do menu.

        pygame.display.flip()

    pygame.quit()