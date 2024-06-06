import pygame

largura = 600
altura = 600
cor_fundo = (0, 0, 0)
velocidade_dudu = 10
velocidade_plataforma = 3
imagemdefundo = pygame.image.load("imagem/favela.jpg")
imagemdefundo2 = pygame.image.load("imagem/galaxia.jpg")
imagemdefundo = pygame.transform.scale(imagemdefundo, (600,820))
imagemdefundo2 = pygame.transform.scale(imagemdefundo2, (600,820))