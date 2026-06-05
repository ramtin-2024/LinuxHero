import pygame
import sys
from src.player import Player

# Game initialization
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(".:: Linux Hero: Virus Escape ::.")
clock = pygame.time.Clock()

# Load and scale terminal environment background
bg_surface = pygame.image.load("assets/images/background.png").convert()
bg_surface = pygame.transform.scale(bg_surface, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Define invisible platforms aligned with the background artwork
# Format: pygame.Rect(X, Y, Width, Height)
platforms = [
    pygame.Rect(0, 540, 450, 40),       # First platform on the left
    pygame.Rect(500, 550, 100, 40),     # Small lower-middle platform
    pygame.Rect(600, 500, 480, 40),     # Main central terminal platform
    pygame.Rect(1167, 470, 110, 40),    # Top-right elevated platform
    pygame.Rect(1080, 550, 40, 40)      # Small step platform on the right
]

# Instantiate player and set initial spawning position on the first platform
player = Player((180, 545)) 
player_group = pygame.sprite.GroupSingle(player)

# Main game loop
while True:
    # Calculate delta time (dt) in seconds for frame-rate independence
    dt = clock.tick(60) / 1000 
    
    # Event handling loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update player state and pass platform hitboxes for physics processing
    player_group.update(dt, platforms)

    # Render graphics
    screen.blit(bg_surface, (0, 0)) 
    player_group.draw(screen)      
    
    # Debug tool: Draw red outlines around hitboxes to verify platform positioning
    # Comment out or remove this loop when you want to hide the red boxes
    for platform in platforms:
        pygame.draw.rect(screen, (255, 0, 0), platform, 2)
    
    # Update full display Surface to the screen
    pygame.display.update()