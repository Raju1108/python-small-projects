''' This program shows the simulation of 5 balls bouncing under gravitational acceleration.
It is also accompanied by elastic collision with walls of the container.
It is a fun to watch '''

import pygame
import time
import random
import requests
from io import BytesIO

pygame.init()

# Setting screen size of Pygame window to 800 by 600 pixels
screen = pygame.display.set_mode((800, 600))

# Function to load image from URL
def load_image_from_url(url):
    response = requests.get(url)
    image = pygame.image.load(BytesIO(response.content)).convert_alpha()  # Use convert_alpha() for transparency
    return image

# Online image URLs
background_url = 'https://upload.wikimedia.org/wikipedia/commons/8/89/HD_transparent_picture.png'
ball_image_url = 'https://upload.wikimedia.org/wikipedia/commons/7/7a/Basketball.png'

# Load images
background = load_image_from_url(background_url)
ball_image = load_image_from_url(ball_image_url)

# Resize the ball image to a smaller size (50x50 pixels)
ball_image = pygame.transform.scale(ball_image, (50, 50))

# Additional Title
pygame.display.set_caption('Ball Bounce Simulation')

class Ball:
    g = 1  # Gravitational acceleration

    def __init__(self):
        self.velocityX = 4
        self.velocityY = 4
        self.X = random.randint(0, 768)
        self.Y = random.randint(0, 350)

    def render_ball(self):
        screen.blit(ball_image, (self.X, self.Y))

    def move_ball(self):
        # Changing y component of velocity due to downward acceleration
        self.velocityY += Ball.g
        # Changing position based on velocity
        self.X += self.velocityX
        self.Y += self.velocityY
        # Collision with the walls changes velocity
        if self.X < 0 or self.X > 768:
            self.velocityX *= -1
        if self.Y < 0 and self.velocityY < 0:
            self.velocityY *= -1
            self.Y = 0
        if self.Y > 568 and self.velocityY > 0:
            self.velocityY *= -1
            self.Y = 568

# List of balls created as objects
Ball_List = [Ball(), Ball(), Ball(), Ball(), Ball()]

# The main program loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    time.sleep(0.02)
    screen.blit(background, (0, 0))
    for ball_item in Ball_List:
        ball_item.render_ball()
        ball_item.move_ball()
    pygame.display.update()
    clock.tick(60)

pygame.quit()
