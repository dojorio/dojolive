import sys, pygame
pygame.init()

size = width, height = 520, 540
speed = [1, 1]
red = 255, 0, 0
white = pygame.Color(255, 255, 255)

screen = pygame.display.set_mode(size)
surface = pygame.Surface((100, 100)) #tamnho do box
surface.fill(red)

for i in range(5000):

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    white.r = white.r - 1 or 255
    white.g = white.g - 5 or 255
    white.b = white.b - 3 or 255
    
    speed = [speed[0] + 1, speed[1] + 1]

    ball = pygame.draw.circle(surface, white, (50, 50), 50)
    # top, left = 0, 0
    ball = ball.move(speed)
    # top, left = 1, 1

    if ball.left < 0 or ball.right > width:
        speed[0] = speed[0]
    if ball.top < 0 or ball.bottom > height:
        speed[1] = -speed[1]

    screen.fill(red)
    screen.blit(surface, ball)
    pygame.display.flip()
