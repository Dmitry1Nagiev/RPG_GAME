import pygame
import sys
from sprites.sprite_classes import *
from camera import Camera
BLACK = (0,0,0)
WIDTH = 800
HEIGHT = 800
MINIMAP_TILE = 5
MINIMAP_POS =(10,10)



FPS = 60
pygame.init()
mapFile = ('game_lvl/Real_world1.txt')

window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('RPG')
clock = pygame.time.Clock()
from load import *

def drawMinimap():
    global game_map, show_mini_map

    for i in range(100):
        for j in range(100):
            tile = game_map[i][j]
            x = MINIMAP_POS[0] + j * MINIMAP_TILE
            y = MINIMAP_POS[1] + i * MINIMAP_TILE
            if tile == '1':
                color = (50,200,50)
            elif tile == '2':
                color = (240,120,50)
            elif tile == '3':
                color = (100,100,100)
            elif tile == '4':
                color = (250,215,155)
            elif tile == '5':
                color = (50,200,240)
            pygame.draw.rect(window,color,(x,y,MINIMAP_TILE,MINIMAP_TILE))
            player_tile_x = int(player.rect.centerx // 80)
            player_tile_y = int(player.rect.centery // 80)

            px = MINIMAP_POS[0] + player_tile_x * MINIMAP_TILE
            py = MINIMAP_POS[1] + player_tile_y * MINIMAP_TILE

            pygame.draw.rect(window,(255,255,255),
                             (px,py,MINIMAP_TILE,MINIMAP_TILE))







open_size = 20
def restart():
    global player_group,player,all_sprites,grass_group,lava_group,rock_group,sand_group,water_group,camera,collision_sprites,blue_cristal_group,red_cristal_group
    player_group = pygame.sprite.Group()
    rock_group = pygame.sprite.Group()
    water_group= pygame.sprite.Group()
    sand_group = pygame.sprite.Group()
    grass_group = pygame.sprite.Group()
    lava_group = pygame.sprite.Group()
    blue_cristal_group = pygame.sprite.Group()
    red_cristal_group = pygame.sprite.Group()
    collision_sprites = pygame.sprite.Group()
    player = Player(player_images['right'][0],(400,400),collision_sprites)

    player_group.add(player)
    camera = Camera(8000,8000,WIDTH,HEIGHT)
    all_sprites = pygame.sprite.Group()
def lvlGame():
    global player_group,player,all_sprites,grass_group,lava_group,rock_group,sand_group,water_group,camera,collision_sprites,blue_cristal_group,red_cristal_group
    blue_crystals = 0
    player_group.update(dt,FPS,player_images)

    camera.update(player,window,all_sprites)
    crystal_collected = pygame.sprite.spritecollide(player,blue_cristal_group,True)
    for crystal in crystal_collected:
        blue_crystals += 1
        i,j = crystal.tile_pos
        game_map[i][j] = '3'
        open_new_area()


    if show_mini_map:
        drawMinimap()
    pygame.display.update()



game_map = []
def loadMap(mapFile):
    global game_map
    with open(mapFile,'r') as file:
        for line in file:
            game_map.append(line.replace('/n', '').split(','))
def drawMap(mapFile):
    global player_group, player, all_sprites, grass_group, lava_group, rock_group, sand_group, water_group,collision_sprites,blue_cristal_group,red_cristal_group

    all_sprites.empty()
    grass_group.empty()
    lava_group.empty()
    rock_group.empty()
    sand_group.empty()
    water_group.empty()
    blue_cristal_group.empty()
    red_cristal_group.empty()
    collision_sprites.empty()


    with open(mapFile, 'r') as file:
        for i in range(100):
            game_map.append(file.readline().replace('\n', '').split(','))

    pos = [0, 0]
    for i in range(open_size):
        pos[1] = i * 80
        for j in range(open_size):
            pos[0] = j * 80
            if game_map[i][j] == '1':
                grass = Grass(grass_image,pos)
                grass_group.add(grass)
                all_sprites.add(grass)
            elif game_map[i][j] == '2':
                rock = Rock(rock_image,pos)
                rock_group.add(rock)
                collision_sprites.add(rock)
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
                collision_sprites.add(water)
                all_sprites.add(water)
            elif game_map[i][j] == '6':
                blue_cristal = Crystal(blue_cristal_image,(pos[0],pos[1]),(i,j))
                blue_cristal_group.add(blue_cristal)
                all_sprites.add(blue_cristal)
            elif game_map[i][j] == '7':
                red_cristal = Crystal(red_cristal_image,(pos[0],pos[1]),(i,j))
                red_cristal_group.add(red_cristal)
                all_sprites.add(red_cristal)
def open_new_area():
    global open_size , all_sprites, camera
    open_size += 20
    player_pos = player.rect.center
    drawMap('game_lvl/Real_world1.txt')
    player.rect.center = player_pos
    player_pos = pygame.Vector2(player_pos)
    all_sprites.add(player)



dt = clock.tick(FPS) / 1000


restart()
loadMap('game_lvl/Real_world1.txt')
drawMap(mapFile)

all_sprites.add(player)

show_mini_map = False

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                show_mini_map = not show_mini_map
    window.fill(BLACK)
    lvlGame()
