import pygame
import sys

# Initialize Pygame
pygame.init()

# Create a display window
screen = pygame.display.set_mode((800, 600))  # Set window size (width x height)
pygame.display.set_caption("Menu")  # Set window caption

# Load and scale the start and exit button images
try:
    background = pygame.image.load('bg.png').convert_alpha()
    background = pygame.transform.scale(background, (800, 600))
    start = pygame.image.load("START.png").convert_alpha()
    start = pygame.transform.scale(start, (350, 150))  # Correct scaling
    exit = pygame.image.load("EXIT.png").convert_alpha()
    exit = pygame.transform.scale(exit, (350, 150))
except pygame.error as e:
    print(f"Error loading images: {e}")
    pygame.quit()
    sys.exit()

# Define the button rects for easy detection
start_rect = start.get_rect(topleft=(200, 100))  # Start button position
exit_rect = exit.get_rect(topleft=(200, 400))   # Exit button position

# Main game loop
running = True

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Exit the game
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Get mouse position
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Check if the start button is clicked
            if start_rect.collidepoint(mouse_x, mouse_y):
                import game

            # Check if the exit button is clicked
            if exit_rect.collidepoint(mouse_x, mouse_y):
                print("Exit button clicked!")
                running = False  # Exit the game

    
    # Draw everything on the screen
    screen.blit(background, (0, 0))  # Draw background
    screen.blit(start, start_rect)    # Draw start button
    screen.blit(exit, exit_rect)      # Draw exit button

    # Update the screen
    pygame.display.update()

# Quit Pygame
pygame.quit()
sys.exit()