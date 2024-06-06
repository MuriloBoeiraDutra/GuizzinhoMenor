import pygame


class Pontos():
    def __init__(self, tela, pontos, settings):
        self.pontos = pontos
        self.settings = settings
        self.tela = tela
        
        self.cor = (255, 255, 255)
        self.fonte = pygame.font.SysFont(None, 48)

    def desenha(self):
        self.mensagem_renderizada = self.fonte.render(str(self.pontos), True, self.cor)
        self.tela.blit(self.mensagem_renderizada, (0,0))
