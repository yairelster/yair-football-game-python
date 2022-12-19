import pygame
import math
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (1, 30, 100)

# This is a simple class that represents a magnet
# It has a position (x and y) and a strength (strength)
class Magnet:
    def __init__(self, x, y, strength):
        self.x = x
        self.y = y
        self.strength = strength

# Initialize Pygame
pygame.init()

# Set the width and height of the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode([screen_width, screen_height])

# Set the title of the window
pygame.display.set_caption('Magnet Game')

# Create two magnets with different strengths
gate = Magnet(random.randint(50, 750), random.randint(50, 550), 12.5)
ball = Magnet(random.randint(50, 750), random.randint(50, 550), 6.25)

# Set the magnet that is being magnetized to ball
magnetized_magnet = ball

# This is the game loop
running = True
while running:
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Draw the magnets
    pygame.draw.circle(screen, WHITE, (gate.x, gate.y), 50)
    pygame.draw.circle(screen, RED, (ball.x, ball.y), 50)

    # Calculate the distance between the two magnets
    distance = ((gate.x - ball.x)**2 + (gate.y - ball.y)**2)**0.5

    # Calculate the force of attraction between the two magnets
    force = gate.strength * ball.strength / distance**2

    # Calculate the angle between the two magnets
    angle = math.atan2(gate.y - ball.y, gate.x - ball.x)

    # Calculate the change in position for the magnetized magnet
    dx = force + math.cos(angle)
    dy = force + math.sin(angle)

    # Update the position of the magnetized magnet based on the force of attraction
    magnetized_magnet.x += dx
    magnetized_magnet.y += dy

    # Update the screen
    pygame.display.flip()

# Quit Pygame
pygame.quit()
