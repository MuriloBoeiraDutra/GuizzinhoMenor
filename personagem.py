import pygame
import settings

vec = pygame.math.Vector2
PLAYER_FRICTION = -0.12

class Player(pygame.sprite.Sprite):
    def __init__(self, tela, x=0, y=0, sizeX=10, sizeY=10):
        super().__init__()
        self.nome_imagem = 'imagem/duduzinho.png'
        self.nome_imagem2 = 'imagem/astronauta.png'
        self.imagem = pygame.transform.scale(pygame.image.load(self.nome_imagem), (45, 65))
        self.imagem2 = pygame.transform.scale(pygame.image.load(self.nome_imagem2), (45, 65))

        self.direction = 'left'

        self.tela = tela
        self.rect = pygame.Rect(x, y, self.imagem.get_rect().width, self.imagem.get_rect().height)

        self.pos = vec(x, y) #ajustar...
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.jumps = 1
        self.playeracc = 2
        self.playerjump = 50
        self.pontos = 0

    def atualiza(self, plataformas , pontos):
        self.acc = vec(0, 1)
        self.events()

        self.acc += self.vel * PLAYER_FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        self.rect.midbottom = self.pos
        self.collideWall(plataformas, pontos)


        if self.rect.top >= self.tela.get_rect().height:
             pygame.quit()
             exit(-1)

    def jump_cut(self):
        if self.jumps > 0:
            if self.vel.y < -3:
                self.vel.y = -3

    def jump(self):
        if self.jumps > 0:
            self.jumps -= 1
            self.vel.y = -self.playerjump

    def collideWall(self, plataformas , pontos):
        hits = pygame.sprite.spritecollide(self, plataformas, False )
        if hits:
            if self.pos.y - hits[0].rect.bottom < 0:
                self.pos.y = hits[0].rect.top
            if self.rect.bottom >= hits[0].rect.top and hits[0].ponto == True:
                hits[0].ponto = False
                pontos.pontos += 1
            self.vel.y = 0
            self.jumps = 1


    def setDirection(self, direction):
        if not self.direction == direction:
            self.direction = direction

    def events(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_d]:
            self.acc.x = self.playeracc
            self.setDirection('left')
        if key[pygame.K_a]:
            self.acc.x = -self.playeracc
            self.setDirection('right')

    def desenha(self, pontos):
        if pontos.pontos < 50:
            self.tela.blit(self.imagem, self.rect)
        else:
            self.tela.blit(self.imagem2, self.rect)