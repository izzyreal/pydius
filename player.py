import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, scale):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sprites/player.png")
        self.image_up = pygame.image.load("sprites/player_up.png")
        self.image_down = pygame.image.load("sprites/player_down.png")
        
        self.rect = self.image.get_rect()
        self.w = self.rect.width * scale
        self.h = self.rect.height * scale
        self.moving_up = False
        self.moving_down = False
    
    def move_up(self):
        self.moving_up = True
        self.rect.y -= 1
  
    def move_down(self):
        self.moving_down = True
        self.rect.y += 1
     
    def move_left(self):
        self.rect.x -= 1
  
    def move_right(self):
        self.rect.x += 1
     
    def draw(self, screen):
        img = self.image
        if self.moving_up:
            img = self.image_up
        if self.moving_down:
            img = self.image_down
                        
        screen.blit(pygame.transform.scale(img, (self.w, self.h)), (self.rect.x, self.rect.y))

    def keys(self, pressed):
        if pressed[pygame.K_UP]:
            self.move_up()
        if pressed[pygame.K_DOWN]:
            self.move_down()
        if pressed[pygame.K_LEFT]:
            self.move_left()
        if pressed[pygame.K_RIGHT]:
            self.move_right()

        if not pressed[pygame.K_UP]:
            self.moving_up = False
        if not pressed[pygame.K_DOWN]:
            self.moving_down = False
            
