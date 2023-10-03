import pygame
import sys
import configparser

'''screen'''
config = configparser.ConfigParser()
config.read(r"config.ini")
for i in config:
    for j in config[i]:
        print(f'[{i}][{j}]{config[i][j]}')
WIDTH, HEIGHT = int(config["INIT"]["WIDTH"]),int(config["INIT"]["HEIGHT"])
FPS = int(config["INIT"]["FPS"])
'''color const'''
SKY_BLUE = (135, 206, 250)
WHITE = (255, 255, 255)
BIRD_COLOR = (255, 0, 0)
'''const for animated objects(bird and cloud)'''
bird_x0 = -50
bird_y0 = 300

cloud_x0 = -200
cloud_y0 = 100
'''vars for animated objects(bird and cloud)'''
bird_x = 100
bird_y = 300
bird_speed = 4

cloud_x = 400
cloud_y = 100
cloud_speed = 1

'''
initialise app window (with title)
'''
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bird Flying")
clock = pygame.time.Clock()

def draw_bird(screen,bird_x,bird_y,color):
    '''
    draw new position of bird
    surface - pygame.display
    bird_x, bird_y - previous position of bird
    color - color of bird
    '''
    pygame.draw.polygon(screen, color, [(bird_x, bird_y), (bird_x + 20, bird_y - 10), (bird_x + 30, bird_y), (bird_x + 20, bird_y + 10)])

def draw_cloud(screen,cloud_x,cloud_y,color):
    '''
    draw new position of cloud
    screen - pygame.display
    cloud_x, cloud_y - previous position of bird
    color - color of cloud
    '''
    cloud_x += cloud_speed

    if cloud_x > WIDTH:
        cloud_x = -200

    pygame.draw.circle(screen, color, (cloud_x, cloud_y), 50)
    pygame.draw.circle(screen, color, (cloud_x + 100, cloud_y - 50), 70)
    pygame.draw.circle(screen, color, (cloud_x + 200, cloud_y), 50)

def move(x0,y0,x,y,obj_speed):
    '''
    animation cycle
    x0,y0 - start position of obj (before first move func call)
    x,y - previous position of obj
    obj_speed - horisontal speed of obj (pixels/tick) used for calc shift
    '''
    x += obj_speed
    if x > WIDTH:
        x = x0
    y = y
    return x,y



running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(SKY_BLUE)

    draw_bird(screen,bird_x,bird_y,BIRD_COLOR)
    draw_cloud(screen,cloud_x,cloud_y,WHITE)

    bird_x,bird_y = move(bird_x0,bird_y0,bird_x,bird_y,bird_speed)
    cloud_x,cloud_y = move(cloud_x0,cloud_y0,cloud_x,cloud_y,cloud_speed)

    pygame.display.flip()
    
pygame.quit()
sys.exit()        
