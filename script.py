import pygame

pygame.init()

window = pygame.display.set_mode((900, 506))
pygame.display.set_caption("stranger")

walkRight = [
    pygame.image.load('adventurer-run-00-1.3.png'),
    pygame.image.load('adventurer-run-01-1.3.png'),
    pygame.image.load('adventurer-run-02-1.3.png'),
    pygame.image.load('adventurer-run-03-1.3.png'),
    pygame.image.load('adventurer-run-04-1.3.png'),
    pygame.image.load('adventurer-run-05-1.3.png')
]
walkLeft = [
    pygame.image.load('run_left_0.png'),
    pygame.image.load('run_left_1.png'),
    pygame.image.load('run_left_2.png'),
    pygame.image.load('run_left_3.png'),
    pygame.image.load('run_left_4.png'),
    pygame.image.load('run_left_5.png')
]
bg = pygame.image.load('background.jpg')
avStand = pygame.image.load('adventurer-idle-00-1.3.png')

timer = pygame.time.Clock()

x = 50  # start point for avatar
y = 415  # start point for avatar
width = 37
height = 50
velocity = 5

jumping = False
jumpCount = 10

left = False
right = False
anmCount = 0


def draw_window():
    global anmCount
    window.blit(bg, (0, 0))

    if anmCount + 1 >= 30:
        anmCount = 0

    if left:
        window.blit(walkLeft[anmCount//5], (x, y))
        anmCount += 1
    elif right:
        window.blit(walkRight[anmCount // 5], (x, y))
        anmCount += 1
    else:
        window.blit(avStand, (x, y))

    pygame.display.update()


run = True
while run:
    timer.tick(30)
    for act in pygame.event.get():
        if act.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 5:
        x -= velocity
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 900 - 5 - width:
        x += velocity
        right = True
        left = False
    else:
        right = False
        left = False
        anmCount = 0
    if not jumping:
        if keys[pygame.K_SPACE]:
            jumping = True
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                y += (jumpCount ** 2) / 2
            else:
                y -= (jumpCount ** 2) / 2
            jumpCount -= 1
        else:
            jumping = False
            jumpCount = 10
    draw_window()


pygame.quit()
