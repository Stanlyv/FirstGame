import pygame
from sys import exit
from random import randint
def display_score():
    current_time = int((pygame.time.get_ticks() - start_time) / 1000)
    score_surf = text_font.render(f"Score: {current_time}", False, text_color)
    score_rect = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf, score_rect)
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 300:
                screen.blit(snail_surf, obstacle_rect)
            else: screen.blit(fly_surf, obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        return obstacle_list
    else:
        return []

def collisions(player, obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True

def player_animation():
    global player_surf, player_index
    # walking animation if player is on the froor
    # Jumping animation if player is not on the floor

    if player_rect.bottom < 300:
        player_surf = player_jump
    else:
        player_index += 0.1
        if player_index > len(player_walk):
            player_index = 0
        player_surf = player_walk[int(player_index)]




pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
text_font = pygame.font.Font("font/pixelType.ttf", 50)
text_color = (64, 64, 64)
box_color = "#c0e8ec"
game_active = False
score = 0

sky_surf = pygame.image.load("graphics/platformerGraphicsDeluxePackOld/sky.png").convert()
sky_surf = pygame.transform.scale(sky_surf, (800, 300))
ground_surf = pygame.image.load("graphics/platformerGraphicsDeluxePackOld/groundAndGrass.png").convert()
ground_surf = pygame.transform.scale(ground_surf, (800, 150))

#Snail
snail_frame_1 = pygame.image.load("graphics/platformerGraphicsDeluxePack/Enemies/snailWalk1.png").convert_alpha()
snail_frame_2 = pygame.image.load("graphics/platformerGraphicsDeluxePack/Enemies/snailWalk2.png").convert_alpha()
snail_frames = [snail_frame_1, snail_frame_2]
snail_frame_index = 0
snail_surf = snail_frames[snail_frame_index]

#Fly
fly_frame_1 = pygame.image.load("graphics/platformerGraphicsDeluxePack/Enemies/flyFly1.png").convert_alpha()
fly_frame_2 = pygame.image.load("graphics/platformerGraphicsDeluxePack/Enemies/flyFly2.png").convert_alpha()
fly_frames = [fly_frame_1, fly_frame_2]
fly_frame_index = 0
fly_surf = fly_frames[fly_frame_index]

obstacle_rect_list = []


player_walk_1 = pygame.image.load("graphics/platformerGraphicsDeluxePack/Player/p1_walk/PNG/p1_walk09.png").convert_alpha()
player_walk_2 = pygame.image.load("graphics/platformerGraphicsDeluxePack/Player/p1_walk/PNG/p1_walk11.png").convert_alpha()
player_walk = [player_walk_1, player_walk_2]
player_index = 0
player_jump = pygame.image.load("graphics/platformerGraphicsDeluxePack/Player/p1_walk/PNG/p1_walk03.png").convert_alpha()

player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom=(80, 300))
player_gravity = 0

#intro screen
player_stand = pygame.image.load("graphics/platformerGraphicsDeluxePack/Player/p1_front.png").convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rect = player_stand.get_rect(center=(400, 200))

game_name = text_font.render("Pixel        Runner", False, (111, 196, 169))
game_name_rect = game_name.get_rect(center= (410, 200))

game_message = text_font.render("Press SPACE to run", False, (111, 196, 169))
game_message_rect = game_message.get_rect(center=(400, 350))

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(fly_animation_timer, 200)


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
                start_time = pygame.time.get_ticks()
        if game_active:
            if event.type == obstacle_timer:
                if randint(0,2):
                    obstacle_rect_list.append(snail_surf.get_rect(midbottom=(randint(900, 1100), 300)))
                else:
                    obstacle_rect_list.append(fly_surf.get_rect(midbottom=(randint(900, 1100), 200)))
            if event.type == snail_animation_timer:
                if snail_frame_index == 0:
                    snail_frame_index = 1
                else:
                    snail_frame_index = 0
                snail_surf = snail_frames[snail_frame_index]
            if event.type == fly_animation_timer:
                if fly_frame_index == 0:
                    fly_frame_index = 1
                else:
                    fly_frame_index = 0
                fly_surf = fly_frames[fly_frame_index]

    if game_active:
        screen.blit(sky_surf, (0, 0))
        screen.blit(ground_surf, (0, 300))
        score = display_score()
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        player_animation()
        screen.blit(player_surf, player_rect)

        #obstacle movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        #collision
        game_active = collisions(player_rect, obstacle_rect_list)

    else:
        screen.fill((94,129,162))
        screen.blit(player_stand, player_stand_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom = (80, 300)
        player_gravity = 0

        score_messege = text_font.render(f"Your score: {score}", False, (111, 196, 169))
        score_messege_rect = score_messege.get_rect(center=(400,350))
        screen.blit(game_name, game_name_rect)

        if score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            screen.blit(score_messege, score_messege_rect)


    pygame.display.update()
    clock.tick(60)