import pygame
import settings as s
from personagem import Player
import funções_jogo as functions
from plataforma import Plataforma
from pontos import Pontos


def main():
    pygame.init()  
    tela = pygame.display.set_mode((s.largura, s.altura))
    pygame.display.set_caption("Guizzinho Menor")
    duduzinho = Player(tela, 300, 300)
    plataformas = pygame.sprite.Group()
    contCriaPlat = 0
    clock = pygame.time.Clock()
    settings = s
    pontos = Pontos(tela , 0 , settings)
    functions.cria_pontos(pontos)
    plataformas.add(Plataforma(tela, True))
    while True:
        clock.tick(90)
        functions.testa_eventos(duduzinho, plataformas)
        functions.atualiza_tela(tela, duduzinho, plataformas, s, pontos)
        duduzinho.atualiza(plataformas , pontos)
        contCriaPlat += 1
        if contCriaPlat == 90:
            plataformas.add(Plataforma(tela))
            contCriaPlat = 0

main()
