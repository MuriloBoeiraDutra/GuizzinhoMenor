import pygame
from pygame.sprite import Sprite
from random import randint
from settings import velocidade_plataforma, altura, largura



class Plataforma(Sprite):
    def __init__(self, tela, platBasica=False):
        super(Plataforma, self).__init__()
        self.tela = tela
        self.nome_imagem = 'imagem/plataforma.png'
        self.nome_imagem2 = 'imagem/quejinho.png'
        self.platBasica = platBasica
        self.ponto = True

        if platBasica:
            self.imagem = pygame.transform.scale(pygame.image.load(self.nome_imagem), (largura, 70))
            self.rect = self.imagem.get_rect()
            self.rect.y = altura
            self.rect.x = 0
        else:
            self.imagem = pygame.transform.scale(pygame.image.load(self.nome_imagem), (100, 70))
            self.imagem2 = pygame.transform.scale(pygame.image.load(self.nome_imagem2), (100, 70))
            self.rect = self.imagem.get_rect()
            self.rect.bottom = 0
            self.rect.x = randint(30, 500)
            self.retangulo_tela = tela.get_rect()


    def desenha(self, pontos):
        if pontos.pontos < 50:
            self.tela.blit(self.imagem, self.rect)
        else:
            self.tela.blit(self.imagem2, self.rect)

    def update(self):
        if not self.platBasica:
            self.rect.y += velocidade_plataforma
            if self.rect.y == self.tela.get_rect().bottom:
                self.kill()
