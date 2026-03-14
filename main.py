import pygame
import sys
from sprites.sprite_classes import *
from camera import Camera
BLACK = (0,0,0)
WIDTH = 800
HEIGHT = 800
FPS = 60
pygame.init()


window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('RPG')
clock = pygame.time.Clock()
from load import *

def restart():
    global player_group,player,all_sprites,grass_group,lava_group,rock_group,sand_group,water_group,camera
    player_group = pygame.sprite.Group()
    rock_group = pygame.sprite.Group()
    water_group= pygame.sprite.Group()
    sand_group = pygame.sprite.Group()
    grass_group = pygame.sprite.Group()
    lava_group = pygame.sprite.Group()
    player = Player(player_images['right'][0],(400,400))

    player_group.add(player)
    camera = Camera(8000,8000,WIDTH,HEIGHT)
    all_sprites = pygame.sprite.Group()
def lvlGame():
    global player_group,player,all_sprites,grass_group,lava_group,rock_group,sand_group,water_group,camera

    player_group.update(dt,FPS,player_images)

    camera.update(player,window,all_sprites)


    pygame.display.update()
def drawMap(mapFile):
    global player_group, player, all_sprites, grass_group, lava_group, rock_group, sand_group, water_group


    game_map = []

    with open(mapFile, 'r') as file:
        for i in range(100):
            game_map.append(file.readline().replace('\n', '').split(','))

    pos = [0, 0]
    for i in range(100):
        pos[1] = i * 80
        for j in range(100):
            pos[0] = j * 80
            if game_map[i][j] == '1':
                grass = Grass(grass_image,pos)
                grass_group.add(grass)
                all_sprites.add(grass)
            elif game_map[i][j] == '2':
                rock = Rock(rock_image,pos)
                rock_group.add(rock)
                all_sprites.add(rock)
            elif game_map[i][j] == '3':
                lava = Lava(lava_image,pos)
                lava_group.add(lava)
                all_sprites.add(lava)
            elif game_map[i][j] == '4':
                sand = Sand(sand_image,pos)
                sand_group.add(sand)
                all_sprites.add(sand)
            elif game_map[i][j] == '5':
                water = Water(water_image,pos)
                water_group.add(water)
                all_sprites.add(water)



dt = clock.tick(FPS) / 1000


restart()
drawMap('game_lvl/Real_world1.txt')

all_sprites.add(player)
while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    window.fill(BLACK)
    lvlGame()
