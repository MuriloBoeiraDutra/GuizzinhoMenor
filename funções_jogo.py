import sys, pygame
import settings




# RESPONDE A EVENTOS OCORRENDO TECLA E MOUSE
def cria_pontos(pontos):
    pontos.desenha()

def testa_eventos(duduzinho, plataformas):
    duduzinho.events()
    for e in pygame.event.get():  # VERIFICA OS EVENTOS OCORRIDOS
        if e.type == pygame.QUIT:  # VERIFICA SE A JANELA FOI FECHADA
            sys.exit()
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_w:
                for plat in plataformas:
                    if plat.platBasica:
                        plat.kill()
                duduzinho.jump()
        if e.type == pygame.KEYUP:
            if e.key == pygame.K_w:
                duduzinho.jump_cut()

        # ATUALIZA AS IMAGENS DA TELA


def atualiza_tela(tela, duduzinho, plataformas, s, pontos):
    tela.fill(settings.cor_fundo)
    if pontos.pontos < 50:
        tela.blit(s.imagemdefundo, (0, 0))
    else:
        tela.blit(s.imagemdefundo2, (0, 0))
    plataformas.update()
    for p in plataformas:
        p.desenha(pontos)
    duduzinho.desenha(pontos)  # DESENHA O PERSONAGEM NA TELA
    pontos.desenha()
    pygame.display.flip()  # REDESENHA A TELA



