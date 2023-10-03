import pygame
import sys


pygame.init()

WIDTH, HEIGHT = 800, 600
SKY_BLUE = (135, 206, 250)
WHITE = (255, 255, 255)
BIRD_COLOR = (255, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bird Flying")

bird_x = 100
bird_y = 300
bird_speed = 0.4

cloud_x = 400
cloud_y = 100
cloud_speed = 0.1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    bird_x += bird_speed
    if bird_x > WIDTH:
        bird_x = -50

    cloud_x += cloud_speed
    if cloud_x > WIDTH:
        cloud_x = -200

    screen.fill(SKY_BLUE)

    pygame.draw.circle(screen, WHITE, (cloud_x, cloud_y), 50)
    pygame.draw.circle(screen, WHITE, (cloud_x + 100, cloud_y - 50), 70)
    pygame.draw.circle(screen, WHITE, (cloud_x + 200, cloud_y), 50)

    pygame.draw.polygon(screen, BIRD_COLOR, [(bird_x, bird_y), (bird_x + 20, bird_y - 10), (bird_x + 30, bird_y), (bird_x + 20, bird_y + 10)])

    pygame.display.flip()

pygame.quit()
sys.exit()
