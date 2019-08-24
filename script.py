import pygame

pygame.init()

window = pygame.display.set_mode((800, 400))
pygame.display.set_caption("stranger")

x = 50  # start point for avatar
y = 330  # start point for avatar
width = 40
height = 60
velocity = 5

run = True
while run:
    pygame.time.delay(100)
    for act in pygame.event.get():
        if act.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 5:
        x -= velocity
    if keys[pygame.K_RIGHT] and x < 800 - 5 - width:
        x += velocity
    if keys[pygame.K_UP] and y > 5:
        y -= velocity
    if keys[pygame.K_DOWN] and y < 400 - height - 5:
        y += velocity

    window.fill((0, 0, 0))
    pygame.draw.rect(window, (0, 0, 255), (x, y, width, height))
    pygame.display.update()

pygame.quit()
