import pygame
from graficos.texturas import TEXTURAS
from graficos.texturas import menu_img


def visualizar_mapa(mapa_, agente=None, caminho=None, nome_algoritmo="", tamanho_mapa=""):
    largura_celula = 32
    altura_celula = 32
    altura_barra_info = 40

    largura_tela = len(mapa_[0]) * largura_celula
    altura_tela = len(mapa_) * altura_celula + altura_barra_info

    tela = pygame.display.set_mode((largura_tela, altura_tela))
    pygame.display.set_caption("Visualização do Mapa")

    fonte = pygame.font.Font(None, 24)
    texto_algoritmo = fonte.render(nome_algoritmo, True, (255, 153, 51))
    texto_tamanho = fonte.render(tamanho_mapa, True, (255, 153, 51))

    indice_caminho = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        tela.fill((255, 255, 255))

        # Desenha a barra de informações usando tiles/parede
        for i in range(0, largura_tela, menu_img.get_width()):
            tela.blit(menu_img, (i, 0))

        tela.blit(texto_algoritmo, (10, 10))
        tela.blit(texto_tamanho, (largura_tela - 10 - texto_tamanho.get_width(), 10))

        # Desenha cada célula/tile
        for y, linha in enumerate(mapa_):
            for x, celula in enumerate(linha):
                tela.blit(TEXTURAS[celula], (x * largura_celula, y * altura_celula + altura_barra_info))

        # Move o agente ao longo do caminho
        if caminho and agente and indice_caminho < len(caminho):
            agente.mover_para(caminho[indice_caminho])
            # Verifica se o agente chegou ao destino deste segmento do caminho
            if agente.x == caminho[indice_caminho].x and agente.y == caminho[indice_caminho].y:
                indice_caminho += 1

        # Desenha o agente
        if agente:
            # Nota: o desenho do agente também é ajustado em altura para considerar a barra de informações
            agente.desenhar(tela, altura_barra_info)

        pygame.display.flip()
        pygame.time.wait(300)  # Adicionado para dar um intervalo entre cada passo


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
