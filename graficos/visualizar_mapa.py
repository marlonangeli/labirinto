import pygame
from graficos.texturas import TEXTURAS


def visualizar_mapa(mapa_, agente=None, caminho=None):
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

    if caminho:
        desenhar_caminho(caminho, tela)

    pygame.quit()


def desenhar_caminho(caminho, tela):

    largura_celula = 32
    altura_celula = 32

    for i in range(len(caminho) - 1):
        atual = caminho[i]
        proximo = caminho[i + 1]
        x1 = atual.x * largura_celula + largura_celula // 2
        y1 = atual.y * altura_celula + altura_celula // 2
        x2 = proximo.x * largura_celula + largura_celula // 2
        y2 = proximo.y * altura_celula + altura_celula // 2
        pygame.draw.line(tela, (255, 165, 0), (x1, y1), (x2, y2), 6)

        pygame.display.flip()
        pygame.time.wait(100)
