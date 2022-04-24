import pygame
import random


def music(nomedamusica):
    pygame.mixer.music.load(nomedamusica)
    pygame.mixer.music.play(-1)


pygame.init()
# Variaveis uteis para o código

prateado = (192, 192, 192)
preto = (0, 0, 0)
branco = (255, 255, 255)

fonte = pygame.font.SysFont("Comic Sams MS", 30)

lado_celula = 150
num_linhas = 4

largura = 800
altura = 600

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("TeslaVsThomas")

telainicio = pygame.image.load('inicio.png')
telainicio1 = pygame.image.load('fala1.png')
telainicio2 = pygame.image.load('fala2.png')
telainicio3 = pygame.image.load('fala3.png')

music('acdcinstrumental.ogg')

jogo_inicio = True
jogo_principal = True
tela1 = False
tela2 = False
tela3 = False

# Tela inicial

while jogo_inicio == True:
    inicio = True
    while inicio == True:
        tela.blit(telainicio, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                inicio = False
                jogo_inicio = False
                jogo_principal = False
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or (
                    event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                inicio = False
                tela1 = True

    while tela1 == True:
        tela.blit(telainicio1, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                tela1 = False
                jogo_inicio = False
                jogo_principal = False
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or (
                    event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                tela1 = False
                tela2 = True

    while tela2 == True:
        tela.blit(telainicio2, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                tela2 = False
                jogo_inicio = False
                jogo_principal = False
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or (
                    event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                tela2 = False
                tela3 = True

    while tela3 == True:
        tela.blit(telainicio3, (0, 0))
        pygame.display.update()
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                tela3 = False
                jogo_inicio = False
                jogo_principal = False
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or (
                    event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                tela3 = False
                jogo_inicio = False

# While principal para a repetição do jogo

while jogo_principal == True:

    tela.fill(prateado)
    fundopontuacao = pygame.image.load('telapontuacao.png')
    tela.blit(fundopontuacao, (600, 0))
    telapontos = pygame.image.load('telapontos.png')
    pygame.display.update()

    # For para criação do traçado da matriz
    for i in range(0, num_linhas):
        for j in range(0, num_linhas):
            pygame.draw.rect(tela, preto, (i * lado_celula, j * lado_celula, lado_celula, lado_celula), 1)

    num_falha = 0
    num_ideia = 0
    conteudo_celula = [[None for i in range(num_linhas)] for j in range(num_linhas)]

    # vai marcar com 'X' 18.75% das celulas
    # vai marcar com 'Y' 37.5% das celulas

    contfalha = 0
    contideia = 0

    for i in range(0, num_linhas):
        for j in range(0, num_linhas):
            if (random.randint(1, 100) <= 18.75 and contfalha < 3):
                conteudo_celula[i][j] = "X"
                num_falha += 1
                contfalha += 1

            elif (random.randint(1, 100) > 18.75 and random.randint(1, 100) <= 56.26 and contideia < 6):
                conteudo_celula[i][j] = "Y"
                num_ideia += 1
                contideia += 1

    # Para cada uma das celulas, verifica o numero de 'Y' ao redor
    for i in range(0, num_linhas):
        for j in range(0, num_linhas):
            if conteudo_celula[i][j] != "Y" and conteudo_celula[i][j] != 'X':
                num_ideias_redor = 0

                # Acima
                if (i - 1 >= 0 and conteudo_celula[i - 1][j]) == 'Y':
                    num_ideias_redor += 1

                # Esquerda
                if (j - 1 >= 0 and conteudo_celula[i][j - 1]) == "Y":
                    num_ideias_redor += 1

                # Direita
                if (j + 1 < num_linhas and conteudo_celula[i][j + 1]) == "Y":
                    num_ideias_redor += 1

                # Abaixo
                if (i + 1 < num_linhas and conteudo_celula[i + 1][j]) == "Y":
                    num_ideias_redor += 1

                conteudo_celula[i][j] = str(num_ideias_redor)

    celula_revelada = [[False for i in range(num_linhas)] for j in range(num_linhas)]

    tesla_ganhou = False
    thomas_ganhou = False
    jogoempatado = False
    pontos1 = 0
    pontos2 = 0
    num_celulas_abertas = 0
    jogo_cancelado = True

    # While para o jogo

    while jogo_cancelado == True:
        for evento in pygame.event.get():
            if (evento.type == pygame.QUIT):
                jogo_cancelado = False
                jogo_principal = False
                jogo_final = False

            tela_mudou = False

            if (evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1):
                # Pega as coordenadas do ponto de clique e calcula a celula
                # celula_x  e celula_y são as coordenadas dos pixels na matriz, para saber qual quadrado foi clicado

                mouse_x, mouse_y = evento.pos

                celula_x = mouse_x // lado_celula
                celula_y = mouse_y // lado_celula

                # Clicou fora da tela
                if celula_x > num_linhas - 1 or celula_y > num_linhas - 1:
                    continue

                # Entrada no if se a celula foi clicada pela primeira vez
                if not celula_revelada[celula_x][celula_y]:
                    tela_mudou = True
                    num_celulas_abertas += 1
                    celula_revelada[celula_x][celula_y] = True

                    # Verificação dos pontos do jogador 1
                    if conteudo_celula[celula_x][celula_y] == "Y" and pontos1 >= 0 and num_celulas_abertas % 2 == 1:
                        pontos1 += 100
                    if conteudo_celula[celula_x][celula_y] == "X" and pontos1 >= 50 and num_celulas_abertas % 2 == 1:
                        pontos1 -= 50

                    # Verificação dos pontos do jogador 2
                    if conteudo_celula[celula_x][celula_y] == "Y" and pontos2 >= 0 and num_celulas_abertas % 2 == 0:
                        pontos2 += 100
                    if conteudo_celula[celula_x][celula_y] == "X" and pontos2 >= 50 and num_celulas_abertas % 2 == 0:
                        pontos2 -= 50

            # Imagens da matriz
            if tela_mudou:
                i, j = celula_x, celula_y

                if (conteudo_celula[i][j] == "Y"):
                    ideiatela = pygame.image.load('ideia.png')
                    ideiatela = pygame.transform.scale(ideiatela, (lado_celula - 1, lado_celula - 1))
                    tela.blit(ideiatela, (lado_celula * i + 1, lado_celula * j + 1))
                elif (conteudo_celula[i][j] == "X"):
                    falhatela = pygame.image.load('falha.png')
                    falhatela = pygame.transform.scale(falhatela, (lado_celula - 1, lado_celula - 1))
                    tela.blit(falhatela, (lado_celula * i + 1, lado_celula * j + 1))
                else:
                    texto = fonte.render(conteudo_celula[i][j] and conteudo_celula[i][j], False, preto)
                    tela.blit(texto, (lado_celula * i + 0.4 * lado_celula, lado_celula * j + 0.4 * lado_celula))

            # Pontuação na tela
            tela.blit(telapontos, (640, 220))
            texto1 = fonte.render('%d pontos' % pontos1, True, branco)
            tela.blit(texto1, (640, 220))

            tela.blit(telapontos, (640, 380))
            texto2 = fonte.render('%d pontos' % pontos2, True, branco)
            tela.blit(texto2, (640, 380))
            pygame.display.update()

        # Mudar a tela de ganhar ou perder
        if num_celulas_abertas == 16 and pontos1 > pontos2:
            tesla_ganhou = True
            jogo_cancelado = False
        elif num_celulas_abertas == 16 and pontos2 > pontos1:
            thomas_ganhou = True
            jogo_cancelado = False
        elif num_celulas_abertas == 16 and pontos1 == pontos2:
            jogoempatado = True
            jogo_cancelado = False

    # Apresentação da tela final
    jogo_final = True
    while jogo_final == True:
        for evento in pygame.event.get():
            if (evento.type == pygame.QUIT):
                jogo_final = False
                jogo_principal = False

            if tesla_ganhou == True:
                nikolateslawin = pygame.image.load('nikolateslawin.png')
                tela.blit(nikolateslawin, (0, 0))
                pygame.display.update()

            if thomas_ganhou == True:
                thomasedisonwin = pygame.image.load('thomasedisonwin.png')
                tela.blit(thomasedisonwin, (0, 0))
                pygame.display.update()

            if jogoempatado == True:
                jogoempatadotela = pygame.image.load('empataram.png')
                tela.blit(jogoempatadotela, (0, 0))
                pygame.display.update()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_s:
                    jogo_final = False
                    jogo_cancelado = True
                    jogo_principal = True

                if evento.key == pygame.K_n:
                    jogo_principal = False
                    jogo_final = False

pygame.quit()
