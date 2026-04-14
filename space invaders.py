import pygame
pygame.init()

WIDTH = 800
HEIGHT = 500
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))

screen.fill("black")

space = pygame.image.load ("Lesson 4 - Space Invaders/images/space.png")
red = pygame.image.load ("Lesson 4 - Space Invaders/images/spaceship_red.png")
yellow = pygame.image.load ("Lesson 4 - Space Invaders/images/spaceship_yellow.png")

yellow1 = pygame.transform.scale(yellow, (50, 50))
yellow2 = pygame.transform.rotate(yellow1, 90)
red1 = pygame.transform.scale(red, (50, 50))
red2 = pygame.transform.rotate(red1, 270)
border = pygame.Rect(390, 0, 20, 500)
yrec = pygame.Rect(40, 245, 50, 50)
rrec = pygame.Rect(710, 245, 50, 50)

def yellowmove():
    if keys_pressed[pygame.K_w] and yrec.y > 0:
        yrec.y -= 2

clock = pygame.time.Clock()

while True:
    clock.tick(FPS)
    screen.blit(space, (0,0))
    pygame.draw.rect(screen, "black", border)
    screen.blit(yellow2, yrec)
    screen.blit(red2, rrec)
    keys_pressed = pygame.key.get_pressed()
    yellowmove()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()