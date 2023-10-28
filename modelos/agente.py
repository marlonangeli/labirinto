import pygame
import random
from graficos.utils.textura import redimensionar, cortar_textura
from utils.os import PERSONAGEM_SHEET_PATH


class Agente:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        sprite_sheet = pygame.image.load(PERSONAGEM_SHEET_PATH)
        self.tempo_ultimo_movimento = pygame.time.get_ticks()
        self.intervalo_movimento = 1000

        # Corta cada imagem do sprite sheet
        self.imagens = {
            'cima': cortar_textura(sprite_sheet, 0, 150, 56, 60),
            'baixo': cortar_textura(sprite_sheet, 0, 0, 56, 60),
            'esquerda': cortar_textura(sprite_sheet, 0, 50, 56, 60),
            'direita': cortar_textura(sprite_sheet, 0, 100, 56, 60),
        }
        self.direcao = 'baixo'  # direção inicial

    def mover_para(self, destino):
        # Movendo para a direita
        if destino.x > self.x:
            self.mudar_direcao('direita')
            self.x += 1
        # Movendo para a esquerda
        elif destino.x < self.x:
            self.mudar_direcao('esquerda')
            self.x -= 1
        # Movendo para cima
        elif destino.y < self.y:
            self.mudar_direcao('cima')
            self.y -= 1
        # Movendo para baixo
        elif destino.y > self.y:
            self.mudar_direcao('baixo')
            self.y += 1    

    def desenhar(self, tela, offset_y=0):
        altura_agente = self.imagens[self.direcao].get_height()
        diferenca_altura = (32 - altura_agente) // 2  # Centraliza o agente no meio da célula
        tela.blit(self.imagens[self.direcao], (self.x * 32, self.y * 32 + diferenca_altura + offset_y))

    def mudar_direcao(self, nova_direcao):
        if nova_direcao in self.imagens:
            self.direcao = nova_direcao

    def mover_aleatoriamente(self, mapa_):
        agora = pygame.time.get_ticks()
        if agora - self.tempo_ultimo_movimento < self.intervalo_movimento:
            return

        direcoes = [('cima', (0, -1)), ('baixo', (0, 1)), ('esquerda', (-1, 0)), ('direita', (1, 0))]
        random.shuffle(direcoes)

        for direcao, (dx, dy) in direcoes:
            novo_x, novo_y = self.x + dx, self.y + dy
            if 0 <= novo_x < len(mapa_[0]) and 0 <= novo_y < len(mapa_) and mapa_[novo_y][novo_x] != "▓":
                self.x, self.y = novo_x, novo_y
                self.mudar_direcao(direcao)
                self.tempo_ultimo_movimento = agora  # Atualiza o tempo do último movimento
                break