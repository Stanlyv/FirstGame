import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
text_font = pygame.font.Font("font/pixelType.ttf", 50)
text_color = (64, 64, 64)
box_color = "#c0e8ec"
game_active = True


sky_surf = pygame.image.load("graphics/platformerGraphicsDeluxePackOld/sky.png").convert()
sky_surf = pygame.transform.scale(sky_surf, (800, 300))
ground_surf = pygame.image.load("graphics/platformerGraphicsDeluxePackOld/groundAndGrass.png").convert()
ground_surf = pygame.transform.scale(ground_surf, (800, 150))

score_surf = text_font.render("My game", False, text_color)
score_rect = score_surf.get_rect(center=(400, 50))

snail_surf = pygame.image.load("graphics/platformerGraphicsDeluxePack/Enemies/snailWalk1.png").convert_alpha()
snail_rect = snail_surf.get_rect(midbottom=(800, 300))

player_surf = pygame.image.load("graphics/platformerGraphicsDeluxePack/Player/p1_walk/PNG/p1_walk09.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))
player_gravity = 0


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    player_gravity = -20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800

    if game_active:
        screen.blit(sky_surf, (0, 0))
        screen.blit(ground_surf, (0, 300))
        pygame.draw.rect(screen, box_color, score_rect)
        pygame.draw.rect(screen, box_color, score_rect, 10)
        screen.blit(score_surf, score_rect)

        pygame.draw.ellipse(screen, "Brown", pygame.Rect(50, 200, 100, 100))

        snail_rect.x -= 4
        if snail_rect.right <= 0:
            snail_rect.left = 800
        screen.blit(snail_surf, snail_rect)

        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surf, player_rect)

        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill("Yellow")


    pygame.display.update()
    clock.tick(60)