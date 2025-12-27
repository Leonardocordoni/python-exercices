import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))

cellSize = 20

#Calculei quantas células cabem na tela
# 800 / 20 = 40 células na horizontal
# 600 / 20 = 30 células na vertical
cols = 800 // cellSize  # 40
rows = 600 // cellSize  # 30
food_col = random.randint(1, cols - 2)  # evita a borda (0 e cols-1)
food_row = random.randint(1, rows - 2)  # evita a borda (0 e rows-1)

clock = pygame.time.Clock()
move_delay_ms = 150     # 150 ms por passo (ajusta a gosto)
last_move_time = 0      # começa parado
direction = (0, 0)      # ou (0, 0) se quiser parada até apertar tecla
running = True

lead_x = 380
lead_y = 280


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
                # cima (W ou seta pra cima)
                if event.key in (pygame.K_UP, pygame.K_w):
                    # só aceita se NÃO está indo pra baixo
                    if direction != (0, 1):
                        direction = (0, -1)

                # baixo (S ou seta pra baixo)
                elif event.key in (pygame.K_DOWN, pygame.K_s):
                    if direction != (0, -1):
                        direction = (0, 1)

                # esquerda (A ou seta esquerda)
                elif event.key in (pygame.K_LEFT, pygame.K_a):
                    if direction != (1, 0):
                        direction = (-1, 0)

                # direita (D ou seta direita)
                elif event.key in (pygame.K_RIGHT, pygame.K_d):
                    if direction != (-1, 0):
                        direction = (1, 0)
                

    # aqui NÃO mexe em direção, só usa
    # só move quando passar tempo suficiente
    ## UPDATE
    current_time = pygame.time.get_ticks()
    if current_time - last_move_time >= move_delay_ms:
        lead_x += direction[0] * cellSize
        lead_y += direction[1] * cellSize
        last_move_time = current_time  # IMPORTANTE: atualiza o timer

        head_col = lead_x // cellSize  # 0..39
        head_row = lead_y // cellSize  # 0..29

        if head_col == 0 or head_col == cols - 1 or head_row == 0 or head_row == rows - 1: # colisao com borda
            running = False

    #Desenho do fundo xadrez direto na tela, não em Surface separada
    for x in range(cols):  # de 0 até 39
        for y in range(rows):  # de 0 até 29
            #Alternância correta do quadriculado
            if (x + y) % 2 == 0:
                color = (0,100,0)  # Verde Bem escuro
            else:
                color = (0,128,0)  # um acima
            
            rect = (x * cellSize, y * cellSize, cellSize, cellSize)
            pygame.draw.rect(screen, color, rect)

    borda = pygame.draw.rect(screen, "black", [0, 0, 800, 600], 6)  # borda preta ao redor da tela
    snake = pygame.draw.rect(screen, "blue", [lead_x, lead_y, 20, 20]),
    fruit = pygame.draw.rect(screen, "red", [0, 0, 15, 15])

    borda
    snake
    # Desenha a snake (por enquanto só um quadrado)
    fruit

    pygame.display.update() 
    clock.tick(60)

pygame.quit()