import pygame
def cortar_textura(imagem, x, y, largura, altura):
    rect = pygame.Rect(x, y, largura, altura)
    subimagem = pygame.Surface(rect.size, pygame.SRCALPHA).convert_alpha()
    subimagem.blit(imagem, (0, 0), rect)
    return subimagem