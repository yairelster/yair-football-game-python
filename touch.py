import pygame
import random

# Initialize pygame
pygame.init()

# Set the window size
window_size = (400, 400)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title of the window
pygame.display.set_caption("Moving Balls")

# Set the radius of the balls
radius = 20

# Set the initial positions and velocities of the balls
ball1_pos = [100, 100]
ball1_vel = [2, 3]

ball2_pos = [200, 200]
ball2_vel = [3, 2]

# Set the colors of the balls
ball1_color = (255, 0, 0)
ball2_color = (0, 0, 255)

# Set the running flag to True
running = True

# Run the game loop
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the positions of the balls
    ball1_pos[0] += ball1_vel[0]
    ball1_pos[1] += ball1_vel[1]

    ball2_pos[0] += ball2_vel[0]
    ball2_pos[1] += ball2_vel[1]

    # Check if the balls have collided
    if (abs(ball1_pos[0] - ball2_pos[0]) < 2*radius) and (abs(ball1_pos[1] - ball2_pos[1]) < 2*radius):
        # Move the balls to a new random location
        ball1_pos = [random.randint(radius, window_size[0]-radius), random.randint(radius, window_size[1]-radius)]
        ball2_pos = [random.randint(radius, window_size[0]-radius), random.randint(radius, window_size[1]-radius)]

    # Check if the balls have collided with the edges of the screen
    if ball1_pos[0] < radius or ball1_pos[0] > window_size[0] - radius:
        ball1_vel[0] = -ball1_vel[0]
    if ball1_pos[1] < radius or ball1_pos[1] > window_size[1] - radius:
        ball1_vel[1] = -ball1_vel[1]

    if ball2_pos[0] < radius or ball2_pos[0] > window_size[0] - radius:
        ball2_vel[0] = -ball2_vel[0]
    if ball2_pos[1] < radius or ball2_pos[1] > window_size[1] - radius:
        ball2_vel[1] = -ball2_vel[1]

    pygame.time.delay(30)

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the balls
    pygame.draw.circle(screen, ball1_color, ball1_pos, radius)
    pygame.draw.circle(screen, ball2_color, ball2_pos, radius)

    # Update the display
    pygame.display.flip()

# Quit pygame
pygame.quit()
