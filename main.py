import pygame
from random import randint as r

pygame.init()

time = 0
win_size = 700
window = pygame.display.set_mode((win_size, win_size))
bird = pygame.Rect(win_size//6, win_size//2, win_size//20, win_size//20)
pygame.display.set_caption('flappy bird')
speed = win_size/120
clock = pygame.time.Clock()
jump = 0
fps = 40 
image = pygame.image.load('bird.png')

while True:
    if time%300 == 0:
        pipes = []
        for i in range(3, 6):
            rand_y = r(win_size//4, win_size-(win_size//3))
            rand_x = (win_size//3)*i
            pipes.append(pygame.Rect(rand_x, 0,                    win_size//15, rand_y))
            pipes.append(pygame.Rect(rand_x, rand_y+(win_size//3), win_size//15, win_size))
        fps += 5
    time += 1

    clock.tick(fps)
 
    window.fill((50,10,255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(1)
 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
        jump = 5 

    if jump > 0:
        bird.y -= speed*2
        jump -= 1

    if jump == 0:
        bird.y += speed

    if not 0 < bird.y < win_size:
        pygame.quit()

    for pipe in pipes:
        pipe.x -= speed
        if bird.colliderect(pipe):
            pygame.quit()
        if 0 >= pipe.x:
            pipe.x = win_size
            
        pygame.draw.rect(window, (0, 255, 0), pipe)

    # pygame.draw.rect(window, (255, 255, 0), bird)
    window.blit(image, (bird.x, bird.y))
    pygame.display.update()