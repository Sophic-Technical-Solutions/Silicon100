import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 600, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Silicon 100 Robotics")

font = pygame.font.SysFont(None, 56)
text = font.render("Silicon 100 Robotics", True, (255, 255, 255))
text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((20, 20, 40))
    screen.blit(text, text_rect)
    pygame.display.flip()
