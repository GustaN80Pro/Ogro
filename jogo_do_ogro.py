import pygame
from sys import exit

pygame.init()

def animacao_personagem():
    global jogador_index

    jogador_index += 0.11
    if jogador_index >= len(jogador_parado_superficies):
        jogador_index = 0
    
    # Desenha o jogador na tela
    tela.blit(jogador_parado_superficies[int(jogador_index)], jogador_retangulo.topleft)

def animacao_ataque1():
    global jogador_index, ataque1_frame, jogador_atacando

    if ataque1_frame < len(jogador_ataque2):
        tela.blit(jogador_ataque2[ataque1_frame], jogador_retangulo)
        ataque1_frame += 1
    else:
        ataque1_frame = 0
        jogador_atacando = False

def animacao_ogro():
    global ogro_index

    ogro_index += 0.11
    if ogro_index >= len(ogro_parado_superficies):
        ogro_index = 0

    # Ajusta a posição do ogro para o lado direito da tela
    ogro_retangulo.x = tamanho[0] - ogro_retangulo.width

    # Desenha o ogro na tela
    tela.blit(pygame.transform.flip(ogro_parado_superficies[int(ogro_index)], True, False), ogro_retangulo.topleft)

tamanho = 1300, 680
tela = pygame.display.set_mode(tamanho)

jogador_index = 0
jogador_parado_superficies = []
jogador_atacando = False
jogador_ataque2 = [] 

# Carrega o jogador parado
for imagem in range(1, 7):
    img = pygame.image.load(f'Protagonista/PERSONAGEM1/PARADO/tile{imagem}.png').convert_alpha()
    img = pygame.transform.scale(img, (500, 500))
    jogador_parado_superficies.append(img)

# Carrega as imagens de ataque
for image in range(1, 7):
    img = pygame.image.load(f'Protagonista/PERSONAGEM1/ATAQUE2/tile{image}.png').convert_alpha()
    img = pygame.transform.scale(img, (500, 500))
    jogador_ataque2.append(img)

# Inicializa o retângulo do jogador
jogador_retangulo = jogador_parado_superficies[jogador_index].get_rect(center=(100, 300))

ogro_index = 0
ogro_parado_superficies = []

# Carrega o ogro parado
for imagem in range(1, 5):
    img = pygame.image.load(f'Personagens Jogaveis/Ogro1/Parado/tile{imagem}.png').convert_alpha()
    img = pygame.transform.scale(img, (600, 500))
    ogro_parado_superficies.append(img)

# Inicializa o retângulo do ogro
ogro_retangulo = ogro_parado_superficies[ogro_index].get_rect(center=(100, 315))

pygame.display.set_caption("Mata Ogro")

relogio = pygame.time.Clock()

principal = pygame.image.load('Cenários/PNG/Battleground4/Bright/principal.png').convert()

# Velocidade do movimento do personagem
movimento_personagem = 5

# Transforma o tamanho da imagem de fundo
principal = pygame.transform.scale(principal, tamanho)

ataque1_frame = 0 

# Loop principal do jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Teclas para atacar
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        jogador_atacando = True
        jogador_index = 0
        ataque1_frame = 0
            
    # Atualiza a posição do jogador com base nas teclas pressionadas
    keys = pygame.key.get_pressed()
    jogador_retangulo.x += (keys[pygame.K_d] - keys[pygame.K_a]) * movimento_personagem
    jogador_retangulo.y += (keys[pygame.K_s] - keys[pygame.K_w]) * movimento_personagem

    jogador_retangulo.x = max(0, min(jogador_retangulo.x, tamanho[0] - jogador_retangulo.width))
    jogador_retangulo.y = max(0, min(jogador_retangulo.y, tamanho[1] - jogador_retangulo.height))

    # Desenha o fundo na tela
    tela.blit(principal, (0, 0))

    if jogador_atacando:
        animacao_ataque1()
    else:
        animacao_personagem()

    animacao_ogro()

    pygame.display.update()
    relogio.tick(60)