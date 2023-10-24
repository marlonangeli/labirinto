import pygame
def redimensionar(imagem, nova_largura, nova_altura):
    return pygame.transform.scale(imagem, (nova_largura, nova_altura))