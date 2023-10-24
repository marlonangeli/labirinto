from graficos.utils.texturas.redimensionar import redimensionar
from graficos.utils.texturas.cortar_textura import cortar_textura

import pygame
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
TEXTURAS = {
    '▓': parede_img,  # Parede
    '$': bau_img,  # Recompensa
    ' ': solido_plano_img,  # SolidoPlano
    'R': rochoso_img,  # Rochoso
    'A': arenoso_img,  # Arenoso
    'P': pantano_img,  # Pantano
    '☺': parede_img  # Agente
}