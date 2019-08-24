import pygame

pygame.init()

window = pygame.display.set_mode((800, 400))
pygame.display.set_caption("stranger")

x = 50  # start point for avatar
y = 50  # start point for avatar
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
    if keys[pygame.K_LEFT]:
        x -= velocity
    if keys[pygame.K_RIGHT]:
        x += velocity
    if keys[pygame.K_UP]:
        y -= velocity
    if keys[pygame.K_DOWN]:
        y += velocity

    window.fill((0, 0, 0))
    pygame.draw.rect(window, (0, 0, 255), (x, y, width, height))
    pygame.display.update()

pygame.quit()
