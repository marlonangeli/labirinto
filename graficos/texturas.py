import pygame
from graficos.utils.textura import cortar_textura, redimensionar
from utils.constantes.mapa import *
from utils.os import SPRITE_SHEET_PATH, CHEST_PATH


sprite_sheet = pygame.image.load(SPRITE_SHEET_PATH)
bau = redimensionar(pygame.image.load(CHEST_PATH), 32, 32)
parede_img = redimensionar(cortar_textura(sprite_sheet, 112, 304, 16, 16), 32, 32)
rochoso_img = redimensionar(cortar_textura(sprite_sheet, 0, 80, 16, 16), 32, 32)
arenoso_img = redimensionar(cortar_textura(sprite_sheet, 128, 192, 16, 16), 32, 32)
madeira_img = redimensionar(cortar_textura(sprite_sheet, 0, 208, 16, 16), 32, 32)
bau_img = madeira_img.copy()
bau_img.blit(bau, (0, 0))
pantano_img = redimensionar(cortar_textura(sprite_sheet, 64, 400, 16, 16), 32, 32)
solido_plano_img = redimensionar(cortar_textura(sprite_sheet, 32, 240, 16, 16), 32, 32)
origem_img = redimensionar(cortar_textura(sprite_sheet, 192, 160, 16, 16), 32, 32)
destino_img = redimensionar(cortar_textura(sprite_sheet, 64, 176, 16, 16), 32, 32)
menu_img = redimensionar(cortar_textura(sprite_sheet, 0, 208, 16, 16), 64, 64)

TEXTURAS = {
    PAREDE: parede_img,
    RECOMPENSA: bau_img,
    SOLIDO: solido_plano_img,
    ROCHOSO: rochoso_img,
    ARENOSO: arenoso_img,
    PANTANO: pantano_img,
    AGENTE: parede_img,
    INICIO: origem_img,
    DESTINO: destino_img,
    MENU: menu_img
}
