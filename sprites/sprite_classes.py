import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self,image,pos):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.Vector2(self.rect.center)
        self.direction = pygame.Vector2()
        self.speed = 300
        self.im_dir = 'right'
        self.frame = 0
        self.timer_anime = 0
        self.anime = False
    def input(self):
        keys = pygame.key.get_pressed()
        self.direction.x = 0
        self.direction.y = 0
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.im_dir = 'right'
        if keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.im_dir = 'left'
        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.im_dir = 'up'
        if keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.im_dir = 'down'
        if self.direction.length() != 0:
            self.direction = self.direction.normalize()
            self.anime =True
        else:
            self.anime = False
    def move(self,dt):
        self.pos+= self.direction * self.speed * dt
        self.rect.center = self.pos
    def animation(self,FPS,player_images):
        if self.anime:
            self.timer_anime += 1
            self.image = player_images[self.im_dir][self.frame]
            if self.timer_anime / FPS > 0.1:
                if self.frame==len(player_images[self.im_dir]) - 1:
                    self.frame = 0
                else:
                    self.frame += 1
                self.timer_anime = 0
    def update(self,dt,FPS,player_images):
        self.input()
        self.move(dt)
        self.animation(FPS,player_images)
class Grass(pygame.sprite.Sprite):
    def __init__(self,image,pos):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=pos)
class Lava(pygame.sprite.Sprite):
    def __init__(self,image,pos):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=pos)
class Rock(pygame.sprite.Sprite):
    def __init__(self,image,pos):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=pos)
class Sand(pygame.sprite.Sprite):
    def __init__(self,image,pos):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=pos)
class Water(pygame.sprite.Sprite):
    def __init__(self,image,pos):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=pos)









