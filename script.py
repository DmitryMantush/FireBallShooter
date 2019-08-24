import pygame

pygame.init()

window = pygame.display.set_mode((800, 400))
pygame.display.set_caption("stranger")

x = 50  # start point for avatar
y = 330  # start point for avatar
width = 40
height = 60
velocity = 5

jumping = False
jumpCount = 10

run = True
while run:
    pygame.time.delay(50)
    for act in pygame.event.get():
        if act.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 5:
        x -= velocity
    if keys[pygame.K_RIGHT] and x < 800 - 5 - width:
        x += velocity
    if not jumping:
        if keys[pygame.K_UP] and y > 5:
            y -= velocity
        if keys[pygame.K_DOWN] and y < 400 - height - 5:
            y += velocity
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


    window.fill((0, 0, 0))
    pygame.draw.rect(window, (0, 0, 255), (x, y, width, height))
    pygame.display.update()

pygame.quit()
