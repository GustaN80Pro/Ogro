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

# Avança para o proximo frame
    jogador_index += 0.11
    if jogador_index > len(jogador_superficies) - 1:
        jogador_index = 0

    if direcao_personagem == 1:
        personagem = pygame.transform.flip(jogador_superficies[int(jogador_index)], True, False)
    else:
        personagem = jogador_superficies[int(jogador_index)]


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
movimento = 0

# Carrega o jogador parado
for imagem in range(1, 7):
    img = pygame.image.load(f'Protagonista/PERSONAGEM1/PARADO/tile{imagem}.png').convert_alpha()
    img = pygame.transform.scale(img, (500, 500))
    jogador_parado_superficies.append(img)

for image in range(1, 8):
    img = pygame.image.load(f'Protagonista/PERSONAGEM1/ANDANDO/Title{image}.png').convert_alpha()
    img = pygame.transform.scale(img, (500, 500))
    movimento.append()

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

# Carrega o jogador andandoda
for imagem in range(1, 7):
    img = pygame.image.load(f'Protagonista/PERSONAGEM1/PARADO/tile{imagem}.png').convert_alpha()
    img = pygame.transform.scale(img, (500, 500))
    jogador_parado_superficies.append(img)

pygame.display.set_caption("Mata Ogro")

relogio = pygame.time.Clock()

principal = pygame.image.load('Cenários/PNG/Battleground4/Bright/principal.png').convert()

# Velocidade do movimento do personagem
movimento_personagem = 5

# Transforma o tamanho da imagem de fundo
principal = pygame.transform.scale(principal, tamanho)

# Loop principal do jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
            
    # Atualiza a posição do jogador com base nas teclas pressionadas
    keys = pygame.key.get_pressed()
    jogador_retangulo.x += (keys[pygame.K_d] - keys[pygame.K_a]) * movimento_personagem
    jogador_retangulo.y += (keys[pygame.K_s] - keys[pygame.K_w]) * movimento_personagem

    jogador_retangulo.x = max(0, min(jogador_retangulo.x, tamanho[0] - jogador_retangulo.width))
    jogador_retangulo.y = max(0, min(jogador_retangulo.y, tamanho[1] - jogador_retangulo.height))

    # Desenha o fundo na tela
    tela.blit(principal, (0, 0))

    animacao_personagem()
    animacao_ogro()

    pygame.display.update()
    relogio.tick(60)
