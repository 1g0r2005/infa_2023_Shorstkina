import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
SKY_BLUE = (135, 206, 250)
WHITE = (255, 255, 255)
BIRD_COLOR = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Static Bird Image")

# Bird parameters
bird_x = 100
bird_y = 300

# Cloud parameters
cloud_x = 400
cloud_y = 100

# Clear the screen
screen.fill(SKY_BLUE)

# Draw the clouds
pygame.draw.circle(screen, WHITE, (cloud_x, cloud_y), 50)
pygame.draw.circle(screen, WHITE, (cloud_x + 100, cloud_y - 50), 70)
pygame.draw.circle(screen, WHITE, (cloud_x + 200, cloud_y), 50)

# Draw the bird
pygame.draw.polygon(screen, BIRD_COLOR, [(bird_x, bird_y), (bird_x + 20, bird_y - 10), (bird_x + 30, bird_y), (bird_x + 20, bird_y + 10)])

# Save the image as a PNG file
pygame.image.save(screen, "bird_image.png")

# Quit Pygame
pygame.quit()
sys.exit()
