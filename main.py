import sys
import pygame

from starfield import Starfield
from player import Player
    
def main():
    
    pygame.init()
    
    scale = 4
    
    screen = pygame.display.set_mode((256 * scale, 240 * scale))

    starfield = Starfield(scale, screen)
    player = Player(scale)
     
    running = True
    
    while running:
        
        pressed = pygame.key.get_pressed()
        player.keys(pressed)
        
        for event in pygame.event.get():
            
            if event.type == pygame.KEYDOWN:
                            
                if event.key == pygame.K_F4 and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                    running = False
                
            if event.type == pygame.QUIT:
                running = False
                
        screen.fill((0, 0, 0))
        
        starfield.draw()
        player.draw(screen)
        
        pygame.display.update()

    pygame.quit()
    sys.exit()

if __name__=="__main__":
    main()
