"""
STAR CATCHER!
Move your rocket to catch falling stars.
Use the LEFT and RIGHT arrow keys to move.

HOW TO PLAY:
- Catch the yellow stars to get points!
- Don't let them fall off the screen!
- Press ESC or close the window to quit.
"""

import pygame
import random

# --- Start up pygame ---
pygame.init()

# --- Screen size (width x height in pixels) ---
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Star Catcher!")

# --- Colors (Red, Green, Blue) ---
BLACK  = (  0,   0,   0)
WHITE  = (255, 255, 255)
YELLOW = (255, 220,   0)
ORANGE = (255, 140,   0)
BLUE   = ( 30, 144, 255)
RED    = (220,  50,  50)

# --- Clock to control how fast the game runs ---
clock = pygame.time.Clock()
FPS = 60

# --- Font for drawing text on screen ---
font = pygame.font.SysFont("Arial", 30, bold=True)


# -------------------------------------------------------
#  ROCKET  (the thing the player controls)
# -------------------------------------------------------
class Rocket:
    WIDTH  = 50
    HEIGHT = 60
    SPEED  = 5        # pixels moved each frame

    def __init__(self):
        # Start in the middle-bottom of the screen
        self.x = SCREEN_WIDTH // 2 - self.WIDTH // 2
        self.y = SCREEN_HEIGHT - self.HEIGHT - 10

    def move(self, keys):
        """Move left or right when arrow keys are held."""
        if keys[pygame.K_LEFT]  and self.x > 0:
            self.x -= self.SPEED
        if keys[pygame.K_RIGHT] and self.x < SCREEN_WIDTH - self.WIDTH:
            self.x += self.SPEED

    def get_rect(self):
        """Return the rectangle area the rocket takes up."""
        return pygame.Rect(self.x, self.y, self.WIDTH, self.HEIGHT)

    def draw(self):
        """Draw a simple rocket shape."""
        rect = self.get_rect()
        # Body
        pygame.draw.rect(screen, ORANGE, rect, border_radius=8)
        # Nose cone (triangle on top)
        nose = [
            (rect.centerx,          rect.top - 20),
            (rect.left,             rect.top + 5),
            (rect.right,            rect.top + 5),
        ]
        pygame.draw.polygon(screen, RED, nose)
        # Window
        pygame.draw.circle(screen, WHITE, rect.center, 10)
        pygame.draw.circle(screen, BLUE,  rect.center,  7)


# -------------------------------------------------------
#  STAR  (things that fall from the sky)
# -------------------------------------------------------
class Star:
    SIZE  = 24
    SPEED = 3   # pixels per frame downward

    def __init__(self):
        # Appear at a random x position at the top
        self.x = random.randint(0, SCREEN_WIDTH - self.SIZE)
        self.y = -self.SIZE      # start just above the screen

    def fall(self):
        """Move the star down each frame."""
        self.y += self.SPEED

    def is_off_screen(self):
        """True if the star has fallen past the bottom."""
        return self.y > SCREEN_HEIGHT

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.SIZE, self.SIZE)

    def draw(self):
        """Draw a simple star shape."""
        cx = self.x + self.SIZE // 2
        cy = self.y + self.SIZE // 2
        # Outer points of the star
        points = []
        for i in range(5):
            import math
            angle_out = math.radians(-90 + i * 72)
            angle_in  = math.radians(-90 + i * 72 + 36)
            points.append((cx + 12 * math.cos(angle_out),
                            cy + 12 * math.sin(angle_out)))
            points.append((cx +  5 * math.cos(angle_in),
                            cy +  5 * math.sin(angle_in)))
        pygame.draw.polygon(screen, YELLOW, points)


# -------------------------------------------------------
#  MAIN GAME LOOP
# -------------------------------------------------------
def main():
    rocket   = Rocket()
    stars    = []            # list of Star objects on screen
    score    = 0
    missed   = 0
    MAX_MISS = 5             # game over after missing this many stars

    # How many frames until we drop a new star
    spawn_timer    = 0
    SPAWN_INTERVAL = 60      # drop a new star every 60 frames (1 second)

    pygame.mixer.music.load("bonus.mp3")
    pygame.mixer.music.play(-1)

    running = True
    while running:

       

        # --- Handle events (keyboard, window close, etc.) ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # --- Update game state ---
        keys = pygame.key.get_pressed()
        rocket.move(keys)

        # Spawn new stars on a timer
        spawn_timer += 1
        if spawn_timer >= SPAWN_INTERVAL:
            stars.append(Star())
            spawn_timer = 0

        # Move every star down; check catches and misses
        for star in stars[:]:          # loop over a copy so we can remove safely
            star.fall()
            if rocket.get_rect().colliderect(star.get_rect()):
                stars.remove(star)     # caught!
                score += 1
            elif star.is_off_screen():
                stars.remove(star)     # missed!
                missed += 1

        # Check for game over
        if missed >= MAX_MISS:
            running = False

        # --- Draw everything ---
        screen.fill(BLACK)                        # clear with black background

        # Draw some background stars (tiny white dots for decoration)
        for dot in [(50, 80), (200, 30), (400, 120), (320, 60), (150, 200),
                    (460, 70), (90, 350), (370, 280)]:
            pygame.draw.circle(screen, WHITE, dot, 2)

        for star in stars:
            star.draw()

        rocket.draw()

        # Draw score and misses
        score_text  = font.render(f"Stars: {score}",            True, YELLOW)
        missed_text = font.render(f"Missed: {missed}/{MAX_MISS}", True, RED)
        screen.blit(score_text,  (10, 10))
        screen.blit(missed_text, (10, 45))

        pygame.display.flip()          # show what we drew
        clock.tick(FPS)                # keep the game at 60 FPS

    # --- Game Over screen ---
    screen.fill(BLACK)
    over_font = pygame.font.SysFont("Arial", 48, bold=True)
    msg1 = over_font.render("GAME OVER!", True, RED)
    msg2 = font.render(f"You caught {score} stars!", True, YELLOW)
    msg3 = font.render("Close the window to exit.", True, WHITE)
    screen.blit(msg1, msg1.get_rect(center=(SCREEN_WIDTH//2, 220)))
    screen.blit(msg2, msg2.get_rect(center=(SCREEN_WIDTH//2, 300)))
    screen.blit(msg3, msg3.get_rect(center=(SCREEN_WIDTH//2, 360)))
    pygame.display.flip()

    # Wait a moment so the player can read the score
    pygame.time.wait(3000)
    pygame.quit()


# Run the game when this file is executed
if __name__ == "__main__":
    main()
