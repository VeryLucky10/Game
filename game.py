import pygame
from player import Player
import pytmx
import pyscroll

class Game:
    
    def __init__(self):
        self.player = Player()
        self.pressed = {}
        self.screen = pygame.display.set_mode((800, 600))
        tmx_data = pytmx.util_pygame.load_pygame('Assets/map/Map002.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 1.5

        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)

    gravity = 0  #0.1

    def game_lose(self):
        pygame.quit()