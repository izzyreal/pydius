import random
import pygame
from pygame.locals import *

NUM_STARS = 40
WHITE = 255, 255, 255
BLACK = 20, 20, 40
LIGHTGRAY = 180, 180, 180
DARKGRAY = 120, 120, 120

class Starfield():

    def __init__(self, scale, screen):
        random.seed()
        self.scale = scale
        self.screen = screen
        
        self.delay = 8
        self.inc = 2
        
        self.stars = []

        for loop in range(0, NUM_STARS):
            star = [random.randrange(0, self.screen.get_width() - 1),
                    random.randrange(0, self.screen.get_height() - 1)]
            self.stars.append(star);

        for loop in range(0, 10):
            self.screen.set_at(self.stars[loop], WHITE)

    def moveStars(self, start, end):
        for loop in range(start, end):
            if (self.stars[loop][0] != 1):
                self.stars[loop][0] = self.stars[loop][0] - 1
            else:
                self.stars[loop][1] = random.randrange(0, self.screen.get_height() - 1)
                self.stars[loop][0] = self.screen.get_width() - 1

    def draw(self):
        
        self.inc += 1

        for loop in range(0, 10):
            self.screen.set_at(self.stars[loop], BLACK)

        self.moveStars(0, 10)

        if (self.inc % 2 == 0):

            for loop in range(11, 20):
                self.screen.set_at(self.stars[loop], BLACK)

            self.moveStars(11, 20)

            for loop in range(11, 20):
                self.screen.set_at(self.stars[loop], LIGHTGRAY)

        if (self.inc % 5 == 0):
            
            for loop in range(21, NUM_STARS):
                self.screen.set_at(self.stars[loop], BLACK)

            self.moveStars(21, NUM_STARS)

            for loop in range(21, NUM_STARS):
                self.screen.set_at(self.stars[loop], DARKGRAY)

        for loop in range(0, 10):
            star = self.stars[loop]
            pygame.draw.rect(self.screen, WHITE, (star[0], star[1], self.scale, self.scale))

        if (self.inc == 500): inc = 2
