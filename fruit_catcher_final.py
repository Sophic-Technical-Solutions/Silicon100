import pygame
import random
import sys

# === STEP 1: INITIALIZATION (Part 1 of Lesson) ===
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Fruit Catcher")
CLOCK = pygame.time.Clock()

# Colors (R, G, B)
SKY_BLUE = (135, 206, 235)
BASKET_COLOR = (139, 69, 19)
FRUIT_COLOR = (255, 69, 0)
TEXT_COLOR = (0, 0, 0)

# Game Variables
score = 0
lives = 3
font = pygame.font.SysFont("Arial", 32)

# === STEP 2: PLAYER BASKET (Part 2 of Lesson) ===
player_width, player_height = 100, 20
player_x = (WIDTH - player_width) // 2
player_y = HEIGHT - 50
player_speed = 7

# Pygame Rect for the player
basket_rect = pygame.Rect(player_x, player_y, player_width, player_height)

# === STEP 3: FALLING FRUIT (Part 3 of Lesson) ===
fruit_size = 30
fruit_x = random.randint(0, WIDTH - fruit_size)
fruit_y = -fruit_size
fruit_speed = 5

# Pygame Rect for the fruit
fruit_rect = pygame.Rect(fruit_x, fruit_y, fruit_size, fruit_size)

# === GAME LOOP ===
running = True
while running:
    # 1. Event Handling (Check for QUIT or Keys)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. Movement (Part 2)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket_rect.left > 0:
        basket_rect.x -= player_speed
    if keys[pygame.K_RIGHT] and basket_rect.right < WIDTH:
        basket_rect.x += player_speed

    # 3. Fruit Falling Logic (Part 3)
    fruit_rect.y += fruit_speed

    # If fruit falls off screen
    if fruit_rect.top > HEIGHT:
        fruit_rect.x = random.randint(0, WIDTH - fruit_size)
        fruit_rect.y = -fruit_size
        lives -= 1 # Lose a life

    # 4. Collision Detection (Part 4)
    if basket_rect.colliderect(fruit_rect):
        score += 1
        # Reset fruit to the top
        fruit_rect.x = random.randint(0, WIDTH - fruit_size)
        fruit_rect.y = -fruit_size
        # Slightly increase speed to make it harder (Part 5)
        fruit_speed += 0.2

    # 5. Drawing (Part 1 & 4)
    SCREEN.fill(SKY_BLUE) # Clear screen with background color
    
    # Draw Basket and Fruit
    pygame.draw.rect(SCREEN, BASKET_COLOR, basket_rect)
    pygame.draw.ellipse(SCREEN, FRUIT_COLOR, fruit_rect) # Drawn as an ellipse for "fruit" look

    # Draw Text (Score & Lives)
    score_surface = font.render(f"Score: {score}", True, TEXT_COLOR)
    lives_surface = font.render(f"Lives: {lives}", True, TEXT_COLOR)
    SCREEN.blit(score_surface, (10, 10))
    SCREEN.blit(lives_surface, (WIDTH - 120, 10))

    # 6. Check Game Over (Part 5)
    if lives <= 0:
        game_over_surface = font.render("GAME OVER! Press Esc to Quit", True, TEXT_COLOR)
        SCREEN.blit(game_over_surface, (WIDTH // 2 - 150, HEIGHT // 2))
        pygame.display.flip()
        # Wait for user to quit or restart
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    waiting = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        waiting = False

    # Update Display
    pygame.display.flip()
    CLOCK.tick(60) # Limits game to 60 FPS

pygame.quit()
sys.exit()
