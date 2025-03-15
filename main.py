import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Save The Spaceship")

# Load images
background = pygame.image.load("bg.png") 
spaceship = pygame.image.load("spaceship.png") 
meteor_img = pygame.image.load("meteor.png") 
star_img = pygame.image.load("star.png") 

# Resize images
spaceship = pygame.transform.scale(spaceship, (100, 100))
meteor_img = pygame.transform.scale(meteor_img, (100, 100))
star_img = pygame.transform.scale(star_img, (100, 100))

class SpaceObject:
    def __init__(self,type):
        self.x = 400
        self.y = 300
        self.type=type

    def draw(self):
        if self.type=='meteor':
            screen.blit(meteor_img, (self.x, self.y))
        else:
            screen.blit(star_img,(self.x,self.y))

# Game loop
running = True

# spaceship position 
spaceship_x = WIDTH // 2
spaceship_y = HEIGHT - 100

while running:
    screen.blit(background, (0, 0))  # Draw background
    screen.blit(spaceship, (spaceship_x, spaceship_y))  # Draw spaceship

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    type=random.choice(['meteor','star'])
    obj=SpaceObject(type)

    obj.draw()

    pygame.display.update()

pygame.quit()
