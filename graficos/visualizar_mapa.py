import pygame
from graficos.texturas import TEXTURAS
from graficos.texturas import menu_img
from modelos.agente import Agente
from modelos.no import No
from utils.constantes import cores
from utils.constantes.dimensoes import TAMANHO_CELULA


def visualizar_mapa(mapa, agente: Agente, caminho: list[list[No]], nome_algoritmo='', tamanho_mapa=''):
    altura_barra_info = 40

    largura_tela = len(mapa[0]) * TAMANHO_CELULA
    altura_tela = len(mapa) * TAMANHO_CELULA + altura_barra_info

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
        for x, linha in enumerate(mapa):
            for y, celula in enumerate(linha):
                tela.blit(TEXTURAS[celula], (x * TAMANHO_CELULA, y * TAMANHO_CELULA + altura_barra_info))

        if agente:
            desenhar_agente(agente, indice_caminho, caminho, tela, altura_barra_info)
            indice_caminho += 1

        if caminho:
            desenhar_caminho(caminho, tela, altura_barra_info)

        pygame.display.flip()
        pygame.time.wait(100)  # Adicionado para dar um intervalo entre cada passo


def desenhar_agente(agente: Agente, indice_caminho, caminho: list[list[No]], tela, altura_barra=40):
    # primeiro nó do caminho
    caminho_completo = [c for subcaminho in caminho for c in subcaminho]

    if indice_caminho >= len(caminho_completo):
        return

    agente.mover_para_no(caminho_completo[indice_caminho])
    # Verifica se o agente chegou ao destino deste segmento do caminho
    if agente.x == caminho_completo[indice_caminho].x and agente.y == caminho_completo[indice_caminho].y:
        indice_caminho += 1

    agente.desenhar(tela, altura_barra)
    pygame.display.flip()


def desenhar_caminho(caminho: list[list[No]], tela, altura_barra=40):
    for subcaminho in caminho:
        desenhar_subcaminho(subcaminho, tela, altura_barra)


def desenhar_subcaminho(caminho: list[No], tela, altura_barra=40):
    for i in range(len(caminho) - 1):
        atual = caminho[i]
        proximo = caminho[i + 1]

        # verifica se o nó atual e o próximo são vizinhos
        if abs(atual.x - proximo.x) > 1 or abs(atual.y - proximo.y) > 1:
            continue
        x1 = atual.x * TAMANHO_CELULA + TAMANHO_CELULA // 2
        y1 = atual.y * TAMANHO_CELULA + TAMANHO_CELULA // 2 + altura_barra
        x2 = proximo.x * TAMANHO_CELULA + TAMANHO_CELULA // 2
        y2 = proximo.y * TAMANHO_CELULA + TAMANHO_CELULA // 2 + altura_barra
        pygame.draw.line(tela, (255, 165, 0), (x1, y1), (x2, y2), 6)

    pygame.display.flip()
