import pygame
from graficos.utils.textura import redimensionar, cortar_textura
from utils.os import PERSONAGEM_SHEET_PATH


class Agente:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        sprite_sheet = pygame.image.load(PERSONAGEM_SHEET_PATH)
        
        # Corta cada imagem do sprite sheet
        self.imagens = {
            'cima': redimensionar(cortar_textura(sprite_sheet, 0, 0, 32, 32), 32, 32),
            'baixo': redimensionar(cortar_textura(sprite_sheet, 0, 0, 32, 32), 32, 32),
            'esquerda': redimensionar(cortar_textura(sprite_sheet, 0, 0, 32, 32), 32, 32),
            'direita': redimensionar(cortar_textura(sprite_sheet, 0, 0, 32, 32), 32, 32),
        }
        self.direcao = 'baixo'  # direção inicial

    def desenhar(self, tela):
        tela.blit(self.imagens[self.direcao], (self.x * 32, self.y * 32))

    def mudar_direcao(self, nova_direcao):
        if nova_direcao in self.imagens:
            self.direcao = nova_direcao