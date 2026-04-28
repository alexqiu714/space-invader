import pygame
pygame.init()

WIDTH = 800
HEIGHT = 500
FPS = 60
font = pygame.font.SysFont("arial", 30)

yellowbullet = []
redbullet = []

screen = pygame.display.set_mode((WIDTH, HEIGHT))

screen.fill("black")

space = pygame.image.load ("Lesson 4 - Space Invaders/images/space.png")
red = pygame.image.load ("Lesson 4 - Space Invaders/images/spaceship_red.png")
yellow = pygame.image.load ("Lesson 4 - Space Invaders/images/spaceship_yellow.png")
yhealth = 10
rhealth = 10

yellow1 = pygame.transform.scale(yellow, (50, 50))
yellow2 = pygame.transform.rotate(yellow1, 90)
red1 = pygame.transform.scale(red, (50, 50))
red2 = pygame.transform.rotate(red1, 270)
border = pygame.Rect(390, 0, 20, 500)
yrec = pygame.Rect(40, 245, 50, 50)
rrec = pygame.Rect(710, 245, 50, 50)

bulletfiring = pygame.mixer.Sound("Lesson 4 - Space Invaders/images/Gun+Silencer.mp3")
collide = pygame.mixer.Sound("Lesson 4 - Space Invaders/images/Grenade+1.mp3")

def yellowmove():
    if keys_pressed[pygame.K_w] and yrec.y > 0:
        yrec.y -= 2
    if keys_pressed[pygame.K_a] and yrec.x > 0: 
        yrec.x -= 2
    if keys_pressed[pygame.K_d] and yrec.x < 340: 
        yrec.x += 2
    if keys_pressed[pygame.K_s] and yrec.y < 450: 
        yrec.y += 2

def redmove():
    if keys_pressed[pygame.K_UP] and rrec.y > 0:
        rrec.y -= 2
    if keys_pressed[pygame.K_LEFT] and rrec.x > 410: 
        rrec.x -= 2
    if keys_pressed[pygame.K_RIGHT] and rrec.x < 750: 
        rrec.x += 2
    if keys_pressed[pygame.K_DOWN] and rrec.y < 450: 
        rrec.y += 2

clock = pygame.time.Clock()

while True:
    clock.tick(FPS)
    screen.blit(space, (0,0))
    pygame.draw.rect(screen, "black", border)
    screen.blit(yellow2, yrec)
    screen.blit(red2, rrec)
    keys_pressed = pygame.key.get_pressed()
    yellowmove()
    redmove()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LALT:
                bulletfiring.play()
                bullet = pygame.Rect(yrec.x + 50, yrec.y + 22, 10, 5)
                yellowbullet.append(bullet)
            if event.key == pygame.K_RALT:
                bulletfiring.play()
                bullet = pygame.Rect(rrec.x - 10, rrec.y + 22, 10, 5)
                redbullet.append(bullet)
    for i in yellowbullet:
        pygame.draw.rect(screen, "yellow", bullet)
        i.x += 10
        if i.colliderect(rrec):
            rhealth -= 1
            collide.play()
            yellowbullet.remove(i)
    yellowhealthtext = font.render("Health: " + str (yhealth), True, "black")
    screen.blit(yellowhealthtext, (10, 10))
    if rhealth <= 0:
        screen.fill("yellow")
        gameover = font.render("Game over, yellow wins!", True, "blue")
        screen.blit(gameover, (255, 20))
        pygame.display.update()
        pygame.time.delay(3000)
        pygame.quit()
    for i in redbullet:
        pygame.draw.rect(screen, "red", bullet)
        i.x -= 10
        if i.colliderect(yrec):
            yhealth -=1
            collide.play()
            redbullet.remove(i)
    redhealthtext = font.render("Health: " + str (rhealth), True, "black")
    screen.blit(redhealthtext, (650, 10))
    if yhealth <= 0:
        screen.fill("yellow")
        gameover = font.render("Game over, red wins!", True, "blue")
        screen.blit(gameover, (255, 20))
        pygame.display.update()
        pygame.time.delay(3000)
        pygame.quit()
    pygame.display.update()