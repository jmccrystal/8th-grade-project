import sys, pygame, time
#setup pygame

#setup pygame

size = width, height = 600, 500
#sets the size of the screen
speed = [100, 100]
#sets how fast the ball moves
black = 100, 100, 100
#when screen goes black, this is the color it goes to

screen = pygame.display.set_mode(size)
#sets the screen variable to the size variable
ball = pygame.image.load("intro_ball.gif")
#sets the ball to the ball image
ballrect = ball.get_rect()
framerate = 100
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                speed[0] = -speed[0]
                speed[1] = -speed[1]

    ballrect = ballrect.move(speed)

    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
    time.sleep(1/framerate)