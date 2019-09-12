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
flyUp = [
    pygame.image.load('adventurer-jump-02-1.3.png'),
    pygame.image.load('adventurer-jump-03-1.3.png')
]
fall = pygame.image.load('adventurer-fall-00-1.3.png')
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
up = False
down = False
anmCount = 0
lastMove = 'right'


class Bullet:
    def __init__(self, x, y, radius, color, direction):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.direction = direction
        self.speed = 8 * direction

    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)


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
    elif up:
        window.blit(flyUp[anmCount // 2], (x, y))
        anmCount += 1
    elif down:
        window.blit(fall, (x, y))
    else:
        window.blit(avStand, (x, y))

    for blt in bullets:
        blt.draw(window)

    pygame.display.update()


run = True
bullets = []

while run:
    timer.tick(30)
    for act in pygame.event.get():
        if act.type == pygame.QUIT:
            run = False

    for blt in bullets:
        if 0 < blt.x < 900:
            blt.x += blt.speed
        else:
            bullets.pop(bullets.index(blt))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RALT]:
        if lastMove == 'right':
            direction = 1
        else:
            direction = -1
        if len(bullets) < 10:
            bullets.append(Bullet(round(x + width // 2), round(y + height // 2),
                                  5, (255, 0, 0), direction))
    if keys[pygame.K_LEFT] and x > 5:
        x -= velocity
        left = True
        right = False
        lastMove = "left"
    elif keys[pygame.K_RIGHT] and x < 900 - 5 - width:
        x += velocity
        right = True
        left = False
        lastMove = 'right'
    else:
        right = False
        left = False
        anmCount = 0
    if not jumping:
        if keys[pygame.K_UP]:
            jumping = True
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                y += (jumpCount ** 2) / 2
                up = True
                down = False
            else:
                y -= (jumpCount ** 2) / 2
                up = False
                down = True
            jumpCount -= 1
        else:
            jumping = False
            up = False
            down = False
            jumpCount = 10
    draw_window()


pygame.quit()
