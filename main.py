import pygame
import time
from game import Game
import pyscroll
import pytmx

pygame.init()

pygame.display.set_caption("---")

background = pygame.image.load('Assets/white_background.png')

game = Game()

clock = pygame.time.Clock()
game.screen.blit(background, (0, 0))

running = True

while running:

    #gravity
    game.player.y_velocity += game.gravity
    game.player.rect.y += game.player.y_velocity
    game.player.rect.x += game.player.x_velocity
    game.player.pos = (game.player.rect.x, game.player.rect.y)

    camera = game.group

    the_x_loc = game.player.rect.x + 2
    the_center = (the_x_loc, 50)
    print(game.player.x_velocity)

    game.group.draw(game.screen)

    game.screen.blit(game.player.image, game.player.rect)

    camera.center(game.player.pos)
    
    pygame.display.flip()

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if game.player.rect.y >= game.player.last_jump_y:
                    game.player.jump()
                else:
                    print("TEST")
    
    if game.player.rect.y > 600 or game.player.rect.y < 0:
        game.game_lose()

    clock.tick(60)
    time.sleep(0.01)

















































# if game.pressed.get(pygame.K_SPACE):
    #     game.player.jump()



# elif event.type == pygame.KEYDOWN:
        #     game.pressed[event.key] = True

        # elif event.type == pygame.KEYUP:
        #     game.pressed[event.key] = False
