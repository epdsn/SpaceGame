import pygame
from random import randint

class CRT:
    def __init__(self, screen_width, screen_height):
        self.tv = pygame.image.load('assets/tv.png').convert_alpha()
        self.tv = pygame.transform.scale(self.tv, (screen_width, screen_height))
        self.width = screen_width
        self.height = screen_height
    
    def create_crt_lines(self):
        line_height = 3
        line_amount = int(self.height / line_height)
        for line in range(line_amount):
            y_pos = line * line_height
            pygame.draw.line(self.tv, 'black', (0,y_pos), (self.width, y_pos), 1)
    
    def draw(self, screen):
        self.tv.set_alpha(randint(75,90))
        self.create_crt_lines()
        screen.blit(self.tv, (0,0))  