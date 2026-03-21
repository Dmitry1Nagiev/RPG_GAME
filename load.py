import pygame

from script import load_image



player_images = {'right': load_image('assets/images/player/right') ,
                 'left':load_image('assets/images/player/left'),
                 'up':load_image('assets/images/player/up'),
                 'down':load_image('assets/images/player/down')}
grass_image = pygame.image.load('assets/images/blocks/grass.png')
lava_image = pygame.image.load('assets/images/blocks/lava.png')
rock_image = pygame.image.load('assets/images/blocks/rock.png')
sand_image = pygame.image.load('assets/images/blocks/sand.png')
water_image = pygame.image.load('assets/images/blocks/water.png')
blue_cristal_image = pygame.image.load('assets/images/blue_crystal.png')
red_cristal_image = pygame.image.load('assets/images/red_crystal.png')
