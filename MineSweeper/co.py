import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dynamic Text Example")

# Font setup
font = pygame.font.SysFont("Arial", 48)

# Score variable
score = 0
last_update_time = time.time()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update score every second
    current_time = time.time()
    if current_time - last_update_time >= 1:
        score += 1
        last_update_time = current_time

    # Render updated text
    font.render(f"Score: {score}", True, (255, 255, 255))
    text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit()
    pygame.display.flip()