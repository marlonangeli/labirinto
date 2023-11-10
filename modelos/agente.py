import pygame

from graficos.utils.textura import cortar_textura
from modelos.no import No
from utils.constantes.mapa import PAREDE
from utils.os import PERSONAGEM_SHEET_PATH


class Agente:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        self.direcao = 'baixo'

        __sprite_sheet = pygame.image.load(PERSONAGEM_SHEET_PATH)
        self.__direcoes = {
            'cima': (0, 1, cortar_textura(__sprite_sheet, 0, 150, 56, 60)),
            'baixo': (0, -1, cortar_textura(__sprite_sheet, 0, 0, 56, 60)),
            'esquerda': (-1, 0, cortar_textura(__sprite_sheet, 0, 50, 56, 60)),
            'direita': (1, 0, cortar_textura(__sprite_sheet, 0, 100, 56, 60))
        }

    def desenhar(self, tela, offset_y=0):
        _, _, imagem = self.__direcoes[self.direcao]
        altura = imagem.get_height()
        diferenca = 32 - altura
        tela.blit(imagem, (self.x * 32, self.y * 32 + diferenca + offset_y))

    def caminhar_aleatoriamente(self, mapa):
        # move o agente aleatoriamente pelo mapa utliizando ticks do pygame
        agora = pygame.time.get_ticks()
        if agora % 1000 == 0:
            direcoes = ['cima', 'baixo', 'esquerda', 'direita']
            direcao = direcoes[agora % len(direcoes)]
            if mapa[self.x, self.y] != PAREDE:
                self.__mudar_direcao(direcao)
                self.x += self.__direcoes[direcao][0]
                self.y += self.__direcoes[direcao][1]

    def mover_para(self, x: int, y: int):
        if x > self.x:
            self.__mudar_direcao('direita')
        elif x < self.x:
            self.__mudar_direcao('esquerda')
        elif y > self.y:
            self.__mudar_direcao('baixo')
        elif y < self.y:
            self.__mudar_direcao('cima')

        self.x = x
        self.y = y

    def mover_para_no(self, no: No):
        self.mover_para(no.x, no.y)

    def __mudar_direcao(self, nova_direcao):
        if nova_direcao in self.__direcoes:
            self.direcao = nova_direcao
