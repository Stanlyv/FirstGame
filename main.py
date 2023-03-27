import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/pixelType.ttf", 50)


sky_surface = pygame.image.load("graphics/platformerGraphicsDeluxePackOld/sky.png")
sky_surface = pygame.transform.scale(sky_surface, (800, 300))

ground_surface = pygame.image.load("graphics/platformerGraphicsDeluxePackOld/groundAndGrass.png")
ground_surface = pygame.transform.scale(ground_surface, (800,150))

text_surface = test_font.render("My game", False, "Black")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))
    pygame.display.update()
    clock.tick(60)