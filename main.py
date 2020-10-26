import pygame

W = 800
H = 600
TEXT1 = (255, 255, 255)
TEXT2 = (255, 230, 0)
SURC = (0, 0, 64)
CP = 1
CW = 370
CH = 100

pygame.init()

pygame.display.set_caption('Текст')
screen = pygame.display.set_mode((W, H))
pygame.mouse.set_visible(False)

font = pygame.font.SysFont('Arial', 60, True, False)
font2 = pygame.font.SysFont('Arial', 35, True, False)


run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                run = False
    screen.fill(SURC)
    screen.blit(font.render('Всем привет', True, TEXT1), (230, 200))
    screen.blit(font2.render('задание на урок', True, TEXT2), (270, 300))
    cube = pygame.Surface((50, 50))
    cube.fill((200, 0, 0))
    screen.blit(cube, (CW, CH))
    if CP == 1:
        CW += 0.1

    pygame.display.update()
